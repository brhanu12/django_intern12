from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator



def blog_list(request):

    query = request.GET.get("q")

    blogs = Blog.objects.filter(
        isPublished=True
    )

    if query:

        blogs = blogs.filter(
            title__icontains=query
        )

    blogs = blogs.order_by("-created_at")

    paginator = Paginator(
        blogs,
        5
    )

    page_number = request.GET.get("page")

    blogs = paginator.get_page(page_number)

    return render(
        request,
        "blog/list.html",
        {
            "blogs": blogs,
            "query": query,
        }
    )


def blog_detail(request, pk):

    blog = get_object_or_404(
        Blog,
        pk=pk
        
    )

    if request.method == "POST":

        form = CommentForm(
            request.POST
        )

        if form.is_valid():

            comment = form.save(
                commit=False
            )

            comment.blog = blog

            comment.author = request.user

            comment.save()

            messages.success(
    request,
    "Comment added successfully!"
)

            return redirect(
    "blog_detail",
    pk=blog.pk
)

    else:

        form = CommentForm()

    return render(
        request,
        "blog/detail.html",
        {
            "blog": blog,
            "form": form,
        }
    )


@login_required
def blog_create(request):

    if request.method == "POST":

        form = BlogForm(
    request.POST,
    request.FILES,
)

        if form.is_valid():

            blog = form.save(commit=False)

            blog.author = request.user

            blog.isPublished = True

            blog.save()

            messages.success(
    request,
    "Blog created successfully!"
)

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

@login_required
def blog_update(request, pk):

    blog = get_object_or_404(
    Blog,
    pk=pk,
    author=request.user
)
    

    if request.method == "POST":

        form = BlogForm(
    request.POST,
    request.FILES,
    instance=blog
)

        if form.is_valid():

            form.save()

            messages.success(
    request,
    "Blog updated successfully!"
)

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

@login_required
def blog_delete(request, pk):

    blog = get_object_or_404(
    Blog,
    pk=pk,
    author=request.user
)

    if request.method == 'POST':

        blog.delete()

        messages.success(
    request,
    "Blog deleted successfully!"
)

    return redirect("blog_list")

    return render(
        request,
        'blog/delete.html',
        {'blog': blog}
    )



@login_required
def comment_edit(request, pk):

    comment = get_object_or_404(
        Comment,
        pk=pk
    )

    if comment.author != request.user:
        return redirect("blog_detail", pk=comment.blog.pk)

    if request.method == "POST":

        form = CommentForm(
            request.POST,
            instance=comment
        )

        if form.is_valid():

            form.save()

            messages.success(
    request,
    "Comment updated successfully!"
)

        return redirect(
    "blog_detail",
    pk=comment.blog.pk
)

    else:

        form = CommentForm(
            instance=comment
        )

    return render(
        request,
        "blog/comment_edit.html",
        {
            "form": form,
            "comment": comment,
        }
    )
@login_required
def comment_delete(request, pk):

    comment = get_object_or_404(
        Comment,
        pk=pk
    )

    # Only the comment owner can delete it
    if comment.author != request.user:
        return redirect(
            "blog_detail",
            pk=comment.blog.pk
        )

    blog_pk = comment.blog.pk

    if request.method == "POST":

        comment.delete()

        messages.success(
    request,
    "Comment deleted successfully!"
)

    return redirect(
    "blog_detail",
    pk=blog_pk
)

    return render(
        request,
        "blog/comment_delete.html",
        {
            "comment": comment,
        }
    )