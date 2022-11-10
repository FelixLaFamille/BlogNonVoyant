from django.urls import path

from .views import index
from posts.views import BlogHome

urlpatterns = [
    path('index/', index, name="blog-index"),
    path('', BlogHome.as_view(), name="home"),
]