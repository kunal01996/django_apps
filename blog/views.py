from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Page

# Create your views here.


class BlogPageListView(ListView):
    model = Page
    template_name = 'blog/pages/home.html'


class BlogPageDetailView(DetailView):
    model = Page
    template_name = 'blog/pages/detail.html'

