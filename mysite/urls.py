from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='/main/', permanent=False)),
    url(r'^/$', RedirectView.as_view(url='/main/', permanent=False)),
    url(r'^main/', include('main.urls', namespace="main")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', RedirectView.as_view(url='/main/', permanent=False))
)
