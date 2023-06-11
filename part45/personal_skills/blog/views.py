from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required


@login_required
def blogs(request):
    works = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'works': works})


def detail(request, work_id):
    work = get_object_or_404(Blog, pk=work_id)
    if request.method == 'GET':
        form = BlogForm(instance=work)
        return render(request, 'blog/details.html', {'work': work, 'form': form})
    else:
        try:
            form = BlogForm(request.POST, instance=work)
            form.save()
            return redirect('blogs')
        except ValueError:
            return render(request, 'blog/details.html', {
                'work': work,
                'form': form,
                'error': 'Неверные данные'})


@login_required
def createblog(request):
    if request.method == "GET":
        return render(request, 'blog/createblog.html', {'form': BlogForm()})
    else:
        try:
            form = BlogForm(request.POST)
            form.save()
            return redirect('blogs')
        except ValueError:
            return render(request, 'createblog', {
                'form': BlogForm(),
                'error': 'Переданы неверные данные. Попробуйте еще раз.'
            })
