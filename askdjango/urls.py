# askdjango/urls.py

from django.conf.urls import include, url
from django.contrib import admin
from bookmark.views import bookmark_list, bookmark_detail
from askdjango.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^bookmark/$', bookmark_list, name='index'),
	url(r'^bookmark/(?P<pk>\d+)/$', bookmark_detail, name='detail'),
#	url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
#	url(r'^blog/', include('blog.urls', namespace='blog')),
	url(r'^$', HomeView.as_view(), name='home'),
]
