from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class BannerImageAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    image = ImageChooserBlock(required=True)


    class Meta:
        template = "blocks/AboutUsBanner.html"
        icon = "edit"
        label = "Title & Image Banner"

class SimpleRichtextBlock(blocks.RichTextBlock):

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = "blocks/richtext_block.html"
        icon = "edit"
        label = "Simple Richtext"

class CardsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True , help_text="Add your title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image",ImageChooserBlock(required=True)),
                ("title",blocks.CharBlock(required=True,max_length=40)),
                ("text",blocks.TextBlock(required=True)),
                ("url_button",blocks.URLBlock(required=False))
            ]
        )
    )

    class Meta:
        template = "blocks/card_block.html"
        icon="placeholder"
        label="Cards"