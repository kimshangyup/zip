from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
	user = models.ForeignKey(User, unique=True)
	name=models.CharField(max_length=30,null=False)
	gender=models.CharField(max_length=30,null=False)
	age=models.CharField(max_length=5,null=False)
	address=models.CharField(max_length=30,null=False)
	channel=models.CharField(max_length=10,null=False)
	introduce=models.CharField(max_length=200,null=False)
	nationality=models.CharField(max_length=20,null=False)
	language=models.CharField(max_length=20,null=False)
	occupation=models.CharField(max_length=20,null=False)
	preference=models.CharField(max_length=30,null=False)
	kakao=models.CharField(max_length=15,null=False)
	created=models.DateTimeField(auto_now_add=True)
