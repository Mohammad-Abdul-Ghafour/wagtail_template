from turtle import title
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from blocks import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

# Create your models here.
class AboutUsPage(Page):
    template = "aboutUs/aboutUs.html"

    content = StreamField(
        [
            ("simple_banner", blocks.BannerImageAndTextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("card_blocks", blocks.CardsBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]


    class Meta:
        verbose_name = "About Us Page"
        verbose_name_plural = "About Us Pages"

