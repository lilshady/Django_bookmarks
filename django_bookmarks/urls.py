from django.conf.urls import patterns, include, url
import sys
import os.path
from django.views.generic import TemplateView
sys.path.append("D:\\django_bookmarks")
from bookmarks.views import *
site_media = os.path.join(os.path.dirname(__file__),'site_media')
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	#Browsing
	(r'^$',main_page),
	(r'^user/(\w+)/$',user_page),
	
	#session management
	(r'^login/$','django.contrib.auth.views.login'),
	(r'^logout/$',logout_page),
	(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':site_media}),
    (r'^register/$',register_page),
	
    (r'^register/success/$',TemplateView.as_view(template_name="registration/register_success.html")),
	
	#Account management
    (r'^save/$',bookmark_save_page),
	
	(r'^tag/([^\s]+)/$',tag_page),
	(r'^tag/$',tag_cloud_page),
	(r'^search/$',search_page),
	#because of some unknown reasons,the js go to save/ajax/tag/autocomplete not ajax/tag/autocomplete
	#and $.browser is deleted since jquery 1.9, we need a migrated js
	(r'^save/ajax/tag/autocomplete/$',ajax_tag_autocomplete),
	(r'^vote/$',bookmark_vote_page),
	(r'^popular/$',popular_page),
	(r'^comments/',include('django.contrib.comments.urls')),
	(r'^bookmark/(\d+)/$',bookmark_page),
)
