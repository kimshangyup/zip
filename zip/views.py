#-*- coding:UTF-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from zip.models import Room
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import re
from django.template import Context, loader
from django.shortcuts import render

def index(request):
	r=Room.objects.all()
	return render_to_response('dangi.html',locals())

def up(request):
	return render_to_response('up.html')


@csrf_exempt
def upload(request, methods=["POST"]):
	r=Room()
	if request.POST['name'] and request.POST['price']:
		r.name=request.POST['name']
		r.price=request.POST['price']
		r.startdate=request.POST['startdate']
		r.enddate=request.POST['enddate']
		r.etc=request.POST['etc']
		r.option=request.POST['option']
		r.kind=request.POST['kind']
		r.save()
		return HttpResponseRedirect('/zip/')
	else:
		return HttpResponse('실패')