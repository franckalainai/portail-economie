from django.shortcuts import render, get_object_or_404
from .models import Actualite, Post
from taggit.models import Tag
from django.db.models import Count

# Create your views here.
def home(request):
    actualites = Actualite.objects.all()
    return render(request, 'home/index.html', {'actualites': actualites})

def post_list(request, tag_slug=None):
    #posts = Post.objects.filter(status="published")
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    return render(request,'home/posts.html',{'posts':posts, 'tag':tag})

def post_detail(request, post):
    post=get_object_or_404(Post,slug=post,status='published')
    #actualite=get_object_or_404(Actualite,slug=actualite,status='published')
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    #return render(request, 'home/detail.html',{'post':post, 'actualite': actualite, 'similar_posts':similar_posts})
    return render(request, 'home/detail.html',{'post':post, 'similar_posts':similar_posts})