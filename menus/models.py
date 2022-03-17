from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from django_extensions.db.fields import AutoSlugField
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import MultiFieldPanel , FieldPanel , InlinePanel , PageChooserPanel , StreamFieldPanel
from wagtail.core.models import Orderable
from wagtail.core.fields import StreamField
from blocks import blocks

class MenuItem(Orderable):
    
    page = ParentalKey("Menu", related_name="menu_items")
    link_title = models.CharField(blank=True,null=True,max_length=50)
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False,blank=True,)

    content = StreamField(
        [
            ("drop_down",blocks.DropDownBlock())
        ],
        null=True,
        blank=True
    )

    panels = [
        FieldPanel("link_title"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
        StreamFieldPanel("content"),
    ]

@register_snippet
class Menu(ClusterableModel):

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title",editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ],heading = "Menu"),
        InlinePanel("menu_items",max_num=4,min_num=1,label="Menu Item")
        # InlinePanel("menu_items",max_num=4,min_num=1,label="Menu Item")
    ]

    def __str__(self):
        return self.title