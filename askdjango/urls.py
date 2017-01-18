# askdjango/urls.py

from django.conf.urls import url
from django.contrib import admin
from bookmark.views import bookmark_list, bookmark_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^bookmarks/$', bookmark_list, name='index'),
	url(r'^bookmarks/(?P<pk>\d+)/$', bookmark_detail, name='detail'),
]
