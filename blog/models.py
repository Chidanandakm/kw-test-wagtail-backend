from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]


class BlogPage(Page):
    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image", null=True, on_delete=models.SET_NULL, related_name="+"
    )
    author = models.CharField(max_length=255, null=True, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("image"),
        FieldPanel("date"),
        FieldPanel("author"),
    ]
