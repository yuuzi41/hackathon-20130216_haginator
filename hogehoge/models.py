from django.db import models

# Create your models here.
class Questions(models.Model):
 id = models.AutoField(primary_key=True)
 content = models.CharField(max_length=200)
 priority = models.IntegerField()
 def __unicode__(self):
  return self.content
 
class Musics(models.Model):
 id = models.AutoField(primary_key=True)
 title = models.CharField(max_length=200)
 artist = models.CharField(max_length=200)
 def __unicode__(self):
  return self.title

class Samples(models.Model):
 question = models.ForeignKey(Questions)
 music = models.ForeignKey(Musics)
 value = models.IntegerField()
 def __unicode__(self):
  return self.music.title + " - " + self.question.content
