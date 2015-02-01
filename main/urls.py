from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^music/', views.MusicView.as_view(), name='music'),
    url(r'^writing/', views.WritingView.as_view(), name='writing')
)