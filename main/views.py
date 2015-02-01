from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from main.models import WritingSample, MusicSample

def index(request):
    template = loader.get_template('main/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template('main/contact.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def music(request):
    template = loader.get_template('main/music.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

class MusicView(generic.ListView):
    template_name = "main/music.html"
    context_object_name = 'music_samples'

    def get_queryset(self):
        return MusicSample.objects.all().filter(archived=False)


class WritingView(generic.ListView):
    template_name = 'main/writing.html'
    context_object_name = 'writing_samples'

    def get_queryset(self):
        return WritingSample.objects.all().filter(archived=False)
