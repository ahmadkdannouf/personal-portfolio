from django.shortcuts import render, get_object_or_404
from .models import Articles

def blogs(request):

    article = Articles.objects.order_by('-date')[:5]
    return render(request, 'blog/blogs.html', {'article':article})

def detail(request, blog_id):
    blog = get_object_or_404(Articles, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})