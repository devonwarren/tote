from django.db import models
from django.conf import settings
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from months.models import Months


class Contributor(models.Model):
    """People contributing to the content"""
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Panel configuration
    content_panels = Page.content_panels + [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        ImageChooserPanel('image'),
    ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Article(Page):
    """Configurations for the various article pages"""

    # Model fields
    body = RichTextField()
    date = models.DateField("Post date")
    theme = models.ForeignKey(
        'months.Months',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article_theme'
    )
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text_by = models.ForeignKey(
        'Contributor',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='text_by'
    )
    art_by = models.ForeignKey(
        'Contributor',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='art_by'
    )
    # Search indexing
    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    # Panel configuration
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('theme'),
        ImageChooserPanel('main_image'),
        MultiFieldPanel(
            [
                FieldPanel('text_by'),
                FieldPanel('art_by'),
            ],
            heading="Attribution",
            classname="collapsible collapsed",
        ),
        FieldPanel('body', classname="full"),
    ]
