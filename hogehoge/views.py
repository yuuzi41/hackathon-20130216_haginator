# Create your views here.
from django.template import Context, loader
from hogehoge.models import Questions, Musics, Samples
from django.http import HttpResponse

def index(request):
	questions = Questions.objects.all().order_by()
	t = loader.get_template('hogehoge/index.html')
	c = Context({
		'questions': questions, 
	})
	return HttpResponse(t.render(c))

def result(request):
	cand_dist = float("infinity")
	cand_song = None
	
	for m in Musics.objects.all():
		dist = 0.0
		for ans_key, ans_val in request.GET.iteritems():
			sample = Samples.objects.filter(question=int(ans_key), music=m.id)
			coeff = 1
			if int(ans_key) < 3:
				coeff = 5
			if len(sample) > 0:
				dist = dist + coeff * ((int(ans_val) - sample[0].value)**2)
		if cand_dist > dist:
			cand_dist = dist
			cand_music = m

	t = loader.get_template('hogehoge/result.html')
        c = Context({
		'music': cand_music, 
	})
	return HttpResponse(t.render(c))

def matrix(request):
	questions = Questions.objects.all()
	musics = Musics.objects.all()

	body = "<table><tr><th></th>"
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
				body = body + "<td>" + str(s[0].value) + "</td>"
			else:
				body = body + "<td></td>"
		body = body + "</tr>\n"
	body = body + "</table>"

	return HttpResponse(body)
