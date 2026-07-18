from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.filter(isPublished=True).order_by('-created_at')

    return render(
        request,
        'blog/list.html',
        {'blogs': blogs}
    )


def blog_detail(request, pk):

    blog = get_object_or_404(
        Blog,
        pk=pk,
        isPublished=True
    )

    return render(
        request,
        'blog/detail.html',
        {'blog': blog}
    )


def blog_create(request):

    if request.method == 'POST':

        Blog.objects.create(

            title=request.POST.get('title'),

            content=request.POST.get('content'),

            isPublished=True

        )

        return redirect('blog_list')

    return render(
        request,
        'blog/create.html'
    )


def blog_update(request, pk):

    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':

        blog.title = request.POST.get('title')

        blog.content = request.POST.get('content')

        blog.save()

        return redirect(
            'blog_detail',
            pk=blog.pk
        )

    return render(
        request,
        'blog/update.html',
        {'blog': blog}
    )


def blog_delete(request, pk):

    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':

        blog.delete()

        return redirect('blog_list')

    return render(
        request,
        'blog/delete.html',
        {'blog': blog}
    )