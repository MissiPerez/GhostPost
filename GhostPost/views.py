from GhostPost.models import Author, Post
from django.shortcuts import render, HttpResponseRedirect, reverse
from GhostPost.forms import AuthorForm, PostForm

sort = True


def index(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'hello.html', {'text': posts})


def addauthor(request):
    html = 'addauthor.html'

    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
            )
            return HttpResponseRedirect(reverse('post'))
    form = AuthorForm()

    return render(request, html, {'form': form})


def addpost(request, *args, **kwargs):
    html = 'addpost.html'

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                title=data['title'],
                description=data['description'],
                author=data['author'],
                boast=data['boast']
            )
            return HttpResponseRedirect(reverse('home'))
    form = PostForm()

    return render(request, html, {'form': form})


def sort(request, *args, **kwargs):
    html = "hello.html"
    items = Post.objects.filter().order_by('-vote_count')
    return render(request, html, {'text': items})


def boast(request, *args, **kwargs):

    html = "hello.html"
    items = Post.objects.filter(boast=True).order_by('-published_date')
    return render(request, html, {'text': items})


def roast(request, *args, **kwargs):

    html = "hello.html"
    items = Post.objects.filter(boast=False).order_by('-published_date')
    return render(request, html, {'text': items})


def addlike(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist():
        return HttpResponseRedirect(reverse('home'))

    post.vote_count += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))


def removelike(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist():
        return HttpResponseRedirect(reverse('home'))

    post.vote_count -= 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

