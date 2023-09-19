from django.urls import path, re_path, include
from .views import BlogListCreateApiView

app_name = "blogs"


urlpatterns = [
    path('',BlogListCreateApiView.as_view(), name='list_blog' )
]