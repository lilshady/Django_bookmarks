from django.contrib.syndication.views import Feed
from bookmarks.models import Bookmark

class RecentBookmarks(Feed):
    title = 'Django Bookmark | Recent Bookmarks'
    link = '/feeds/recent/'
    description = 'Recent bookmarks posted to Django Bookmarks'
    def items(self):
        return Bookmark.objects.order_by('id')[:10]
    

