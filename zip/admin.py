from django.contrib import admin
from zip.models import Room
# Register your models here.


#admin.site.register(Room)


class RoomAdmin(admin.ModelAdmin):
	list_display=['id','name','address','price','startdate','enddate','option']
	list_filter=['price','address']
	list_display_links=['id','name']
	search_fields=['name','address','option']
	ordering=['-created']


admin.site.register(Room,RoomAdmin)