"""Streamfields live in here."""

from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

from wagtail.blocks import (
    BooleanBlock,
    CharBlock,
    ListBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
    StructValue,
)

from .serializers import WagtailDocumentSerializer, WagtailImageSerializer


class APIImageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        return WagtailImageSerializer(context=context).to_representation(value)


class APIDocumentChooserBlock(DocumentChooserBlock):
    def get_api_representation(self, value, context=None):
        return WagtailDocumentSerializer(context=context).to_representation(value)


class TitleAndTextBlock(StructBlock):
    """Title and text and nothing else."""

    title = CharBlock(required=True, help_text="Add your title")
    text = TextBlock(required=False, help_text="Add subtitle or additional text")

    class Meta:  # noqa
        icon = "edit"
        label = "Title & Text"


class LinkStructValue(StructValue):
    """Additional logic for our urls."""

    def url(self):
        link_url = self.get("link_url")
        if link_url:
            return link_url

        return "#"


class CTABlock(StructBlock):
    """A simple call to action lint or button"""

    text = CharBlock(
        required=True,
        default="Learn More",
        max_length=40,
        help_text="This is the text that appears on the link or button",
    )

    link_url = URLBlock(
        required=False,
        help_text="If the link page above is selected, that will be used first.",  # noqa
    )
    open_in_new_tab = BooleanBlock(default=False, required=False)

    class Meta:  # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"
        value_class = LinkStructValue


class MediaBlock(StreamBlock):
    """Media block: image or document."""

    image = APIImageChooserBlock(required=False)
    document = APIDocumentChooserBlock(required=False)

    class Meta:  # noqa
        icon = "media"
        label = "Media"
        min_num = 1
        max_num = 1


class SimpleCardBlock(StructBlock):
    """Simple card block."""

    title_and_text = TitleAndTextBlock(
        required=True, help_text="Add your title and text for this card"
    )
    media = MediaBlock(required=False, help_text="Add an image or document")
    button_link = CTABlock(required=False)

    class Meta:  # noqa
        icon = "placeholder"
        label = "Simple Card"


"""
Landing page blocks live below here.
"""


class ExploreSectionBlock(StructBlock):
    """Explore section block for landing page."""

    title_and_text = TitleAndTextBlock(
        required=True, help_text="Add your title and subtitle for the explore section"
    )
    cards = ListBlock(SimpleCardBlock, required=False, help_text="Add about cards")

    class Meta:  # noqa
        icon = "edit"
        label = "Explore Section"


class CategoriesSectionBlock(StructBlock):
    """Categories section block for page."""

    title_and_text = TitleAndTextBlock(
        required=True, help_text="Add your title and text"
    )
    categories = ListBlock(CharBlock, required=False, help_text="Add categories")

    class Meta:  # noqa
        icon = "form"
        label = "Categories Section"


class LandingPageBlock(StreamBlock):
    """Landing page block."""

    media = MediaBlock(required=False)
    link = CTABlock(required=False)
    text_and_title = TitleAndTextBlock(required=False)
    card = SimpleCardBlock(required=False)
    logos = ListBlock(APIImageChooserBlock, required=False, help_text="Add brand logos")
    explore_section = ExploreSectionBlock(required=False)
    categories_section = CategoriesSectionBlock(required=False)

    class Meta:  # noqa
        icon = "grip"
        label = "Landing Page"
