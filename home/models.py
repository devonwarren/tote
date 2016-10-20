from __future__ import absolute_import, unicode_literals
from datetime import date
from dateutil.relativedelta import relativedelta
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, \
    MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from articles.models import Article, Contributor
from months.models import Month


class HomePage(Page):
    parent_page_types = []

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)

        try:
            prev = date.today() - relativedelta(months=1)
            prev_month = Month.objects.get(
                year=prev.year,
                month=prev.month)
        except ObjectDoesNotExist:
            prev_month = False

        context['articles'] = Article.objects.live().order_by('-date')
        context['prev_month'] = prev_month
        return context


# placeholder page to be parent to all articles
class ArticleIndexPage(Page):
    parent_page_types = ['HomePage', ]
    subpage_types = ['articles.Article', ]


class AboutPage(Page):
    body = RichTextField()
    feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='feature_image'
    )
    feature_text = RichTextField()

    # Panel configuration
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        MultiFieldPanel(
            [
                ImageChooserPanel('feature_image'),
                FieldPanel('feature_text'),
            ],
            heading="Feature",
            classname="collapsible collapsed",
        ),
        InlinePanel('about_team_members', label="Team Members"),
    ]

    parent_page_types = ['HomePage', ]

    subpage_types = []

    def get_context(self, request):
        context = super(AboutPage, self).get_context(request)
        context['team_members'] = self.about_team_members.all
        return context


class AboutPageTeamLink(Orderable):
    page = ParentalKey(AboutPage, related_name='about_team_members')
    contributor = models.ForeignKey(Contributor)
    position = models.CharField(max_length=120)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('contributor'),
        ImageChooserPanel('image'),
        FieldPanel('position'),
    ]
