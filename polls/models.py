# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.




class Question(models.Model):
	title=models.CharField(max_length=40,null=False)
	Choice=models.IntegerField(default=0,null=True)
	created=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title

class Choice(models.Model):
	options=models.CharField(max_length=20,null=False)
	questions=models.ForeignKey(Question)
	selected=models.IntegerField(default=0,null=True)


class New(models.Model):
	text=models.CharField(max_length=30,null=False)