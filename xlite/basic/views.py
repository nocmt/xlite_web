from basic.models import Articles
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView


# Create your views here.

class IndexView(ListView):
    model = Articles
    template_name = 'basic/index.html'
    context_object_name = 'articles'
    paginate_by = 5

class ArticleView(DetailView):
    model = Articles
    template_name = 'basic/article.html'
    context_object_name = 'article'