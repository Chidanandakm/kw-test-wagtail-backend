from .serializers import BlogPageListSerializer, BlogPageDetailSerializer
from rest_framework import generics

from .models import BlogPage


class BlogListAPIView(generics.ListAPIView):
    serializer_class = BlogPageListSerializer
    queryset = BlogPage.objects.live()


class BlogDetailAPIView(generics.RetrieveAPIView):
    serializer_class = BlogPageDetailSerializer
    queryset = BlogPage.objects.live()
    lookup_field = "slug"
