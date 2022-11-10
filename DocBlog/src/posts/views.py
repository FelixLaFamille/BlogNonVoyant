from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
