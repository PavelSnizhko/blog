from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag

from .models import Post
from django.views import View
from django.views.generic import ListView

from django.http import Http404
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()

        return context


class HomeView(TagMixin, ListView):
    template_name = 'index.html'
    model = Post
    paginate_by = '10'
    context_object_name = 'posts'


class SingleArticle(TagMixin, ListView):
    template_name = 'single_article.html'
    model = Post
    context_object_name = 'article'


    def get_queryset(self):
        return get_object_or_404(Post, pk=self.kwargs.get('id'))



class TagIndexView(TagMixin, ListView):
    template_name = 'index.html'
    model = Post
    paginate_by = '10'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))
