#this file is dedicated to putting the models into admin page
from django.contrib import admin
from models import Link,Bookmark,Tag,SharedBookmark
class BookmarkAdmin(admin.ModelAdmin):
	list_display=['title','link','user']
	list_filter=["user"]
	ordering = ['title']
	search_fields = ['title']

admin.site.register(Link)
admin.site.register(Bookmark,BookmarkAdmin)
admin.site.register(Tag)
admin.site.register(SharedBookmark)
