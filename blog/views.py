from django.shortcuts import render,get_object_or_404

from blog.models import Post


def blog_view(request):
    posts=Post.objects.filter(status=True)
    context={'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_detail_view(request,pid):
    post=get_object_or_404(Post,pk=pid,status=True)
    context={'post':post}
    return render(request, 'blog/blog-single.html',context)
