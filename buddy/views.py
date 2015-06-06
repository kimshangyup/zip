#-*- coding:UTF-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import re
from django.template import Context, loader
from django.shortcuts import render

"""


def show(request, resource_id):
	product = Product.objects.get(id=resource_id)
	comments = product.comment_set.all()
	return render_to_response('show.html', locals(), RequestContext(request))

def comment(request):
	product = Product.objects.get(id=request.POST['product'])
	Comment.objects.create(user=request.user, product=product, content=request.POST['comment'])
	return HttpResponseRedirect('/product/%s' % product.id)

def delete_comment(request, resource_id):
	comment = Comment.objects.get(id=resource_id)
	product_id = comment.product.id
	comment.delete()
	return HttpResponseRedirect('/product/%s' % product_id)

@login_required
def favorite(request, resource_id):
	product = Product.objects.get(id=resource_id)
	Favorite.objects.get_or_create(user=request.user, product=product)
	return HttpResponseRedirect('/favorites')

@login_required
def favorites(request):
	favorites = Favorite.objects.filter(user=request.user)
	return render_to_response('favorites.html', locals())

"""


def average(values):
  if len(values) == 0:
    return None
  return sum(values, 0.0) / len(values)

def aimq(request):
	return render_to_response('aimq.html')

def recommend(request):
	return render_to_response('recommend.html')

def youtravel(request):
	return render_to_response('youtravel.html')

def dangi(request):
	return render_to_response('dangi.html')

def about(request):
	return render_to_response('about.html')

def aim(request):
	return render_to_response('aim.html')

def index(request):
	u=User.objects.last()
	return render_to_response('buddymain.html',locals())

def login(request):
	return render_to_response('login.html',locals(), RequestContext(request))

def around(request):
	d=UserDetail.objects.all()
	return render_to_response('around.html',locals(),RequestContext(request))

#로그인
@csrf_exempt
def authenticate(request):
	user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
	if user == None:
		return HttpResponse('username or password error')
	auth.login(request, user)
	return HttpResponseRedirect('/buddy/')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/buddy/')

def intro(request):
	return render_to_response('intro.html',locals(), RequestContext(request))

def procedure(request):
	return render_to_response('procedure.html',locals(), RequestContext(request))

def signup(request):
	return render_to_response('signup.html',locals(), RequestContext(request))

def detail(request):
	
	return render_to_response('detail.html',locals(), RequestContext(request))

@csrf_exempt
def createdetail(request):
	try:
		ua=User.objects.get(username=request.POST['username'])
		u=UserDetail()
		u.username=ua
		u.name=request.POST['name']
		u.gender=request.POST['gender']
		u.occupation=request.POST['occupation']
		u.nationality=request.POST['nationality']
		u.language=request.POST['language']
		u.age=request.POST['age']
		u.address=request.POST['address']
		u.channel=request.POST['channel']
		u.introduce=request.POST['introduce']
		u.preference=request.POST['preference']
		u.kakao=request.POST['kakao']
		u.save()
		return HttpResponse('응답이 기록되었습니다 <a href="/buddy/">메인 화면으로 가기</a>')
	except:
		return HttpResponse('모든 데이터를 입력하셔야 합니다 <a href="/detail/">이전 화면으로 가기</a>')

def python(request):
	return render_to_response('python.html')

def python1(request):
	return render_to_response('python1.html')

#회원가입
@csrf_exempt
def create(request):
	try:

		user = User.objects.create_user(username=request.POST['username'], 
										email=request.POST['email'],
										password=request.POST['password'])
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		auth.login(request, user)
		return HttpResponseRedirect('/detail/')
	except:
		return HttpResponse('정보를 입력해주세요')

def sowe(request):
	return render_to_response('sowe.html')