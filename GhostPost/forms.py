from GhostPost.models import Author, Post
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'boast']


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']
