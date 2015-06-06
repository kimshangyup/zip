from django.db import models

# Create your models here.


class Room(models.Model):
	name=models.CharField(max_length=30,null=False)
	address=models.CharField(max_length=30,null=False)
	price=models.CharField(max_length=12,null=False)
	startdate=models.CharField(max_length=10,null=False)
	enddate=models.CharField(max_length=10,null=False)
	kind=models.CharField(max_length=30,null=False)
	option=models.CharField(max_length=20,null=False)
	etc=models.CharField(max_length=200,null=False)
	created=models.DateTimeField(auto_now_add=True)