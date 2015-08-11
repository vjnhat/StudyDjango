__author__ = 'FRAMGIA\le.cong.phuc'
from django.shortcuts import render
from framgia.models.blog import Blog


def index(request):
    latest_blog_list = Blog.objects.order_by('-blog_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'blog/index.html', context)


def detail(request,blog_id):
    try:
        blog =Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return render(request, '404.html', {})
    return render(request, 'blog/detail.html', {'blog': blog})