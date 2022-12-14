# Generated by Django 4.1.2 on 2022-10-22 20:08

import aurore.apps.cms.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.blocks.field_block
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0002_homepage_ctas_alter_homepage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "logos",
                        wagtail.blocks.ListBlock(
                            aurore.apps.cms.blocks.APIImageChooserBlock,
                            help_text="Add brand logos",
                            required=False,
                        ),
                    ),
                    (
                        "explore_section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title_and_text",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(
                                                    help_text="Add your title",
                                                    required=True,
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(
                                                    help_text="Add subtitle or additional text",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        help_text="Add your title and subtitle for the explore section",
                                        required=True,
                                    ),
                                ),
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        aurore.apps.cms.blocks.SimpleCardBlock,
                                        help_text="Add about cards",
                                        required=False,
                                    ),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        "project_section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title_and_text",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(
                                                    help_text="Add your title",
                                                    required=True,
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(
                                                    help_text="Add subtitle or additional text",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        help_text="Title and subtitle for project section",
                                        required=True,
                                    ),
                                ),
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        aurore.apps.cms.blocks.SimpleCardBlock,
                                        help_text="Add items",
                                        required=False,
                                    ),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        "categories_section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title_and_text",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(
                                                    help_text="Add your title",
                                                    required=True,
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(
                                                    help_text="Add subtitle or additional text",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        help_text="Add your title and text",
                                        required=True,
                                    ),
                                ),
                                (
                                    "categories",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.field_block.CharBlock,
                                        help_text="Add categories",
                                        required=False,
                                    ),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                ],
                blank=True,
                use_json_field=True,
                verbose_name="content block",
            ),
        ),
    ]
