from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, commentaire
from .forms import CommentForm


# Create your views here.
def articles_home(request):
    posts = Post.objects.all()
    return render(request, 'articles/index.html', {'posts': posts})


def details(request, slug):
    comment = commentaire.objects.all()
    x = Post.objects.get(slug=slug)
    commented = CommentForm
    user_comment = None
    if request.method == 'POST':
        commented = CommentForm(request.POST)
        if commented.is_valid():
            user_comment = commented.save(commit=False)
            user_comment.post = x
            user_comment.save()

    context = {
        'commented': commented,
        'x': x,
        'comment': comment,
    }

    return render(request, 'articles/post.html', context)


def about(request):
    return render(request, "articles/about.html")
