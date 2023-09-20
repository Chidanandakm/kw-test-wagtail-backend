from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView

app_name = "blogs"


urlpatterns = [
    path("", BlogListAPIView.as_view(), name="list_blog"),
    path("<slug:slug>/", BlogDetailAPIView.as_view(), name="detail_blog"),
]
