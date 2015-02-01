from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from blog.models import BlogPost, BlogComment

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return BlogPost.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog_post.html'


def add_comment(request, blog_id):
    p = get_object_or_404(BlogPost, pk=blog_id)
    try:
        comment_title = request.POST['comment_title']
        comment_text = request.POST['comment_text']
        comment_user = request.POST['comment_user']
        if not comment_text:
            return render(request, 'blog/blog_post.html', {
                'blog_id': p.id,
                'error_message': "You didn't enter a comment title.",
            })
        if not comment_title:
            return render(request, 'blog/blog_post.html', {
                'blog_id': p.id,
                'error_message': "You didn't enter a comment title.",
            })
        if not comment_user:
            return render(request, 'blog/blog_post.html', {
                'blog_id': p.id,
                'error_message': "You didn't enter a username.",
            })
    except KeyError:
        return Http404("Something went wrong")
    newcomment = BlogComment()
    newcomment.blogpost = p
    newcomment.text = comment_text
    newcomment.comment_title = comment_title
    newcomment.comment_user = comment_user
    newcomment.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('blog:blogpost', args=(p.id,)))
