from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class BannerImageAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    image = ImageChooserBlock(required=True)


    class Meta:
        template = "blocks/AboutUsBanner.html"
        icon = "edit"
        label = "Title & Image Banner"
