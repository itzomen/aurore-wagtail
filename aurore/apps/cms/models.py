"""Wagtail Models"""
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Orderable, Page

from .blocks import LandingPageBlock, CTABlock


class CorePage(Page):
    """Core Page Model"""

    class Meta:
        abstract = True


class HomePageCarouselImages(Orderable):
    """Home page carousel."""

    page = ParentalKey("HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [FieldPanel("carousel_image")]

    api_fields = [
        APIField("page"),
        APIField("carousel_image"),
    ]


class HomePage(CorePage):
    """
    The Home Page
    """

    parent_page_type = ["wagtailcore.Page"]

    headline = models.CharField(
        max_length=255, help_text="Write the headline for your website"
    )
    sub_headline = models.CharField(
        max_length=255, help_text="Write the sub-headline for your website"
    )
    ctas = StreamField(
        [
            ("cta", CTABlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
        verbose_name="call of action",
        help_text="The Call to Actions Buttons on your page",
    )

    body = StreamField(
        LandingPageBlock(),
        verbose_name="content block",
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("headline", classname="full"),
                FieldPanel("sub_headline"),
            ],
            heading="Hero",
        ),
        MultiFieldPanel(
            [InlinePanel("carousel_images", label="Image")],
            heading="Carousel Images",
            classname="collapsible",
        ),
        FieldPanel("body"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(Page.promote_panels, heading="SEO Settings"),
            ObjectList(Page.settings_panels, heading="Settings"),
        ]
    )

    api_fields = [
        APIField("headline"),
        APIField("sub_headline"),
        APIField("carousel_images"),
        APIField("body"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "homepage"
