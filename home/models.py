from __future__ import absolute_import, unicode_literals
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from articles.models import Contributor


class HomePage(Page):
    pass


class AboutPage(Page):
    body = RichTextField()

    # Panel configuration
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        InlinePanel('about_team_members', label="Team Members"),
    ]

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
