from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator
from wagtail.wagtailsearch import index


class Month(index.Indexed, models.Model):
    """
    These are the months that can be selected from other models and given theme
    """
    MONTHS = (
        (1, 'January'),
        (2, 'Febuary'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )

    theme = models.CharField(max_length=60, help_text="Month theme label")
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField(validators=[MinValueValidator(2010)])

    leader = models.ForeignKey(
        'articles.Article',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='leader',
        help_text='Leader of the Month',
        limit_choices_to={'live': True}
    )
    feature_girl_1 = models.ForeignKey(
        'articles.Article',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='feature_girl_1',
        help_text='Feature Girl #1'
    )
    feature_girl_2 = models.ForeignKey(
        'articles.Article',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='feature_girl_2',
        help_text='Feature Girl #2'
    )
    music_spotlight = models.ForeignKey(
        'articles.Article',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='music_spotlight',
        help_text='Music Spotlight'
    )

    # Search indexing
    search_fields = [
        index.SearchField('theme', partial_match=True, boost=10),
        index.FilterField('year'),
    ]

    class Meta:
        unique_together = (('month', 'year'), )

    def __str__(self):
        return self.MONTHS[self.month][1] + ' ' + str(self.year) + \
            ' ' + self.theme

    def get_absolute_url(self):
        return '/month/' + slugify(self.theme)
