from django.contrib.syndication.views import Feed
from bookmarks.models import Bookmark
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
class RecentBookmarks(Feed):
    title = 'Django Bookmark | Recent Bookmarks'
    link = '/feeds/recent/'
    description = 'Recent bookmarks posted to Django Bookmarks'
    def items(self):
        return Bookmark.objects.order_by('id')[:10]

class UserBookmarks(Feed):
     def get_object(self,request,user):
         #if len(user) != 1:
             #raise ObjectDoesNotExist
         return User.objects.get(username=user)
     def title(self,user):
         return 'Django Bookmarks | Bookmarks for %s' % user.username
     def link(self,user):
     	return '/feeds/user/%s/' %user.username
     def description(self,user):
     	return 'Recent Bookmarks posted by %s' % user.username
     def items(self,user):
     	return user.bookmark_set.order_by('-id')[:10]
    

