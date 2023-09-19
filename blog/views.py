from django.shortcuts import render

# Create your views here.

from .serializer import BlogPageSerializer
from rest_framework import generics
# from rest_framework.permissions import IsAdminUser

from .models import BlogPage

class BlogListCreateApiView(generics.ListCreateAPIView):
    serializer_class = BlogPageSerializer
    queryset = BlogPage.objects.live()