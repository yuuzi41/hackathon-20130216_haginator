from django.template import Context, loader
from hogehoge.models import Questions, Musics, Samples
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
	questions = Questions.objects.all().order_by('priority')
	t = loader.get_template('hogehoge/index.html')
	c = Context({
		'questions': questions, 
	})
	return HttpResponse(t.render(c))

def result(request):
	cand_dist = float("infinity")
	cand_song = None
	cand_songs = [(cand_dist, cand_song)]
	
	for m in Musics.objects.all():
		dist = 0.0
		for ans_key, ans_val in request.GET.iteritems():
			sample = Samples.objects.filter(question=int(ans_key), music=m.id)
			
			# weighted 2-norm
			coeff = 1
			if int(ans_key) < 3:
				coeff = 5
			if len(sample) > 0:
				dist = dist + coeff * ((int(ans_val) - sample[0].value)**2)
		if cand_dist > dist:
			cand_dist = dist
			cand_song = m
		candlistlen = 9 if (len(cand_songs)-1)>9 else len(cand_songs)-1
		if cand_songs[candlistlen][0] > dist:
			for var in range(0, 9 if len(cand_songs)>9 else len(cand_songs)):
				if cand_songs[var][0] > dist:
					cand_songs.insert(var, (dist, m))
					break

	t = loader.get_template('hogehoge/result.html')
	c = Context({
		'music' : cand_song, 
		'list'  : cand_songs
	})
	return HttpResponse(t.render(c))

def matrix(request):
	questions = Questions.objects.all()
	musics = Musics.objects.all()

	body = "<form method=\"POST\" action=\"edit\">"
	body = body + "<table><tr><th></th>"
	for q in questions:
		body = body + "<th>" + q.content + "</th>"
	body = body + "</tr>\n"
	for m in musics:
		body = body + "<tr><td>"+m.title+"</td>"
		for qq in questions:
			s = Samples.objects.filter(question=qq.id, music=m.id)
			if len(s) > 1:
				body = body + "<td>multiple</td>"
			elif len(s) > 0:
				body = body \
				+ "<td align=\"center\"><input type=\"text\" size=\"3\" name=\""\
				+ str(s[0].id) \
				+ "\" value =\"" \
				+ str(s[0].value) \
				+ "\"></td>"
			else:
				body = body + "<td align=\"center\"><input type=\"text\" size=\"3\" name=\"" \
				+ "undef" + str(m.id) + ";" + str(qq.id) + "\" value= \"\" /></td>"
		body = body + "</tr>\n"
	body = body + "</table>"
	body = body + "<input type=\"submit\" /></form>" 

	return HttpResponse(body)

#TODO: remove csrf exempt before public release.
@csrf_exempt
def edit(request):
	body = ""
	for key, value in request.POST.iteritems():
		if str(key).startswith("undef"):
			if value != "":
				mqid = str(key).replace("undef", "").split(";")
				music = Musics.objects.get(id=mqid[0])
				question = Questions.objects.get(id=mqid[1])
				body += "<div id=\"context\">set " \
				+ str(music) + " is " + str(question) \
				+ " as " + str(value) + "</div>"
				Samples(question=question, music=music, value=value).save()
		else:
			sample = Samples.objects.get(id=key)
			if sample.value != int(value):
				body += "<div id=\"context\">update " \
				+ str(sample.music) + " is " + str(sample.question) \
				+ " set " + str(sample.value) + " to " + str(value) \
				+ "</div>"
				sample.value = value
				sample.save()
	return HttpResponse(body)