from django.db import models

# Create your models here.


class Club(models.Model):
	title=models.CharField(max_length=20,null=False)
	text1=models.CharField(max_length=200,null=False)
	text2=models.CharField(max_length=200,null=True)
	contact=models.CharField(max_length=200,null=True)