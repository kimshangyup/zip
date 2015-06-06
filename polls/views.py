#-*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from polls.models import Choice, Question, New
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext
# Create your views here.
import urllib
from bs4 import BeautifulSoup
import datetime

def test_mobile(request):
	url=urllib.urlopen('http://cba.snu.ac.kr/ko/notice')
	soup=BeautifulSoup(url)
	ul=[]
	lu={}
	ll={}
	today=str(datetime.date.today())
	for i in soup.find_all('tr'):
		for a in i.find_all('td','date'):
			if a.text==today:
				lu[i.find_all('td','title')[0].text]=i.find_all('a')[0]['href']
	for i in soup.find_all('tr'):
		for a in i.find_all('td','date'):
			ll[i.find_all('td','title')[0].text]=i.find_all('a')[0]['href']
	context = {'urllist':lu,'today':today,'urllistold':ll}
	template = 'test_mobile.html'
	return render(request, template, context)


def index(request):
	template='index.html'
	context={}
	return render(request,template,context)

def poll(request):
	template='poll.html'
	q=Question.objects.all()
	c=Choice.objects.all()
	context={'q':q,'c':c}
	return render(request,template,context)

@csrf_exempt
def choice(request,offset,methods=['POST']):
	offset=int(offset)
	q=Question.objects.get(id=offset)
	option=request.POST["poll"]
	c=Choice.objects.get(questions=q,id=option)
	c.selected+=1
	c.save()
	return HttpResponseRedirect('/poll')

@csrf_exempt
def write_new(request, methods=['POST']):
	if request.POST['question'] and request.POST['choice1'] and request.POST['choice2']:
		q=Question()
		q.title=request.POST['question']
		q.save()
		c1=Choice()
		c1.questions=q
		c1.options=request.POST['choice1']
		c1.save()
		c2=Choice()
		c2.questions=q
		c2.options=request.POST['choice2']
		c2.save()
		if request.POST['choice3']:
			c3=Choice()
			c3.questions=q
			c3.options=request.POST['choice3']
			c3.save()
			if request.POST['choice4']:
				c4=Choice()
				c4.questions=q
				c4.options=request.POST['choice4']
				c4.save()
				if request.POST['choice5']:
					c5=Choice()
					c5.questions=q
					c5.options=request.POST['choice5']
					c5.save()
	return HttpResponseRedirect('/poll/')

@csrf_exempt
def write(request):
	return render_to_response('write.html', RequestContext(request))

def test(request):
	nn=New.objects.all()
	context={'nn':nn}
	return render(request,'test.html',context)


def test_write(request,methods=['GET','POST']):
	n=New()
	n.text=request.POST['text']
	n.save()
	nn=New.objects.all()
	return HttpResponseRedirect('/test/',{'nn':nn})
