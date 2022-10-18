"""Streamfields live in here."""

from wagtail.blocks import CharBlock, ListBlock, StreamBlock, StructBlock, TextBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

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

    class Meta:  # noqa
        icon = "placeholder"
        label = "Simple Card"


"""
Landing page blocks live below here.
"""


class AboutSectionBlock(StructBlock):
    """About section block for landing page."""

    title_and_text = TitleAndTextBlock(
        required=True, help_text="Add the title and subtitle for this section"
    )
    cards = ListBlock(SimpleCardBlock, required=False, help_text="Add about cards")

    class Meta:  # noqa
        icon = "edit"
        label = "About Section"


class ExploreSectionBlock(StructBlock):
    """Explore section block for landing page."""

    title_and_text = TitleAndTextBlock(
        required=True, help_text="Add your title and subtitle for the explore section"
    )
    cards = ListBlock(
        MediaBlock, required=False, help_text="Add medias for the explore section"
    )

    class Meta:  # noqa
        icon = "edit"
        label = "Explore Section"


class HowItWorksSectionBlock(StructBlock):
    """How it works section block for landing page."""

    title_and_text = TitleAndTextBlock(
        required=True, help_text="Add title and subtitle for this section"
    )
    cards = ListBlock(SimpleCardBlock, required=False, help_text="Add cards")

    class Meta:  # noqa
        icon = "placeholder"
        label = "How It Works Section"


class ProjectRoadMapSectionBlock(StructBlock):
    """Project roadmap section block for landing page."""

    title_and_text = TitleAndTextBlock(
        required=True, help_text="Title and subtitle for project roadmap section"
    )
    cards = ListBlock(SimpleCardBlock, required=False, help_text="Add roadmap items")

    class Meta:  # noqa
        icon = "edit"
        label = "Project Roadmap Section"


class CategoriesSectionBlock(StructBlock):
    """Categories section block for landing page."""

    title_and_text = TitleAndTextBlock(
        required=True, help_text="Add your title and text"
    )
    categories = ListBlock(CharBlock, required=False, help_text="Add categories")

    class Meta:  # noqa
        icon = "form"
        label = "Categories Section"


class LandingPageBlock(StreamBlock):
    """Landing page block."""

    brand_logos = ListBlock(
        APIImageChooserBlock, required=False, help_text="Add brand logos"
    )
    about_section = AboutSectionBlock(required=False)
    explore_section = ExploreSectionBlock(required=False)
    how_it_works_section = HowItWorksSectionBlock(required=False)
    project_roadmap_section = ProjectRoadMapSectionBlock(required=False)
    categories_section = CategoriesSectionBlock(required=False)

    class Meta:  # noqa
        icon = "grip"
        label = "Landing Page"
