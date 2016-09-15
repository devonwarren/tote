from django.db import models


class Months(models.Model):
    """These are the months that can be selected from other models and given themes"""
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
    month = models.CharField(max_length=3, choices=MONTHS)
    year = models.IntegerField()

    def __str__(self):
        return str(self.month + ' ' + self.theme)
