# -*- coding:utf-8 -*-
from django.contrib import admin
from polls.models import Question, Choice, New
# Register your models here.

#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(New)


class QuestionAdmin(admin.ModelAdmin):
	list_display=['id','title','created','Choice']
	list_filter=['title']
	list_display_links=['id','title']
	search_fields=['title']
	ordering=['-created']

class ChoiceAdmin(admin.ModelAdmin):
	list_display=['id','options','questions','selected']
	list_display_links=['id','questions']


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
