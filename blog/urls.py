from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    # ex: /blog/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /blog/1/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='blogpost'),
    # ex: /blog/1/addcomment
    url(r'^(?P<blog_id>\d+)/addcomment/$', views.add_comment, name='addcomment'),


)