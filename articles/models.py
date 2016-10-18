from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from wagtail.wagtailcore.models import Page, PageManager
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from autoslug import AutoSlugField


class Contributor(models.Model, index.Indexed):
    """People contributing to the content"""
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='__str__')

    # Search indexing
    search_fields = [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
    ]

    def save(self, *args, **kwargs):
        if not len(self.slug.strip()):
            self.slug = slugify(self.first_name + ' ' + self.last_name)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('author', kwargs={'slug': self.slug})


class Article(Page):
    """Configurations for the various article pages"""

    # Model fields
    body = RichTextField()
    date = models.DateField("Post date")
    theme = models.ForeignKey(
        'months.Month',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article_theme',
    )
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    main_image_float = models.BooleanField(
        default=False,
        verbose_name='Float Image',
        help_text="Select if the image should float vertically on the details page",
    )
    text_by = models.ForeignKey(
        'Contributor',
        null=False,
        blank=False,
        related_name='text_by',
        on_delete=models.PROTECT,
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
        index.RelatedFields('text_by', [
            index.SearchField('first_name'),
            index.SearchField('last_name'),
        ]),
        index.RelatedFields('art_by', [
            index.SearchField('first_name'),
            index.SearchField('last_name'),
        ]),
    ]

    # Panel configuration
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('theme'),
        MultiFieldPanel(
            [
                ImageChooserPanel('main_image'),
                FieldPanel('main_image_float'),
            ],
            heading="Image",
        ),
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

    objects = PageManager()

    parent_page_types = ['home.ArticleIndexPage', ]
    subpage_types = []

    def get_absolute_url(self):
        return self.url
