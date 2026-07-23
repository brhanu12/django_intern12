from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm


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

    if request.method == "POST":

        form = BlogForm(request.POST)

        if form.is_valid():

            blog = form.save(commit=False)

            blog.isPublished = True

            blog.save()

            return redirect("blog_list")

    else:

        form = BlogForm()

    return render(
        request,
        "blog/create.html",
        {
            "form": form
        }
    )


def blog_update(request, pk):

    blog = get_object_or_404(
        Blog,
        pk=pk
    )

    if request.method == "POST":

        form = BlogForm(
            request.POST,
            instance=blog
        )

        if form.is_valid():

            form.save()

            return redirect("blog_list")

    else:

        form = BlogForm(
            instance=blog
        )

    return render(
        request,
        "blog/update.html",
        {
            "form": form,
            "blog": blog
        }
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