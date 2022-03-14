from turtle import title
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from blocks import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

# Create your models here.
class AboutUsPage(Page):
    template = "aboutUs/aboutUs.html"

    subtitle = models.CharField(max_length=100, blank=False, null=False)

    content = StreamField(
        [
            ("simple_banner", blocks.BannerImageAndTextBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]


    class Meta:
        verbose_name = "About Us Page"
        verbose_name_plural = "About Us Pages"