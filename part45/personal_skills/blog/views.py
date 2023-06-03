from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogs(request):
    works = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'works': works})


def detail(request, work_id):
    work = get_object_or_404(Blog, pk=work_id)
    return render(request, 'blog/details.html', {'work': work})
