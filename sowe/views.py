#-*- coding:UTF-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from sowe.models import Club
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
import md5
import datetime


def my(request):
	return render_to_response('my.html')


def you(request):
	cb=Club.objects.all()[::-1]
	return render_to_response('you.html',{'cb':cb})

@csrf_exempt
def register(request):
	cb=Club()
	cb.title=request.POST['title']
	cb.text1=request.POST['text1']
	cb.text2=request.POST['text2']
	cb.contact=request.POST['contact']
	cb.save()
	return HttpResponseRedirect('/you/')

def each(request,offset):
	offset=int(offset)
	cb=Club.objects.filter(id=offset)
	return render_to_response('yours.html',{'cb':cb})
