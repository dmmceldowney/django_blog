from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post, Tag
from django.http import HttpRequest

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-publish_date')[:5]
    return render(request, 'blog/index.html', {'posts': posts})

# view for ALL blog posts: this will take in arguments (tag IDs) or NO arguments
class BlogView(View):
    template_name = 'blog/blog.html'

    def get(self, request, tag_id=None):
        if tag_id == None:
            posts = Post.objects.filter(tags__).order_by('-publish_date')[:10]
        else:
            posts = Post.objects.filter(tag_pk__in=tag_id)[:10]
        return render(request, self.template_name, {'posts': posts})

# view for blog post
class PostView(View):
    template_name = 'blog/post.html'

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, self.template_name, {'post': post})

# view for about
def about(request):
    return render(request, 'blog/about.html')

# view(s) for tarot services
def process(request):
    return render(request, 'blog/process.html')