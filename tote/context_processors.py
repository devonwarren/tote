from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from months.models import Month


def this_month(request):
    if not cache.get('this_month'):
        try:
            this_month = Month.objects.get(
                year=date.today().year,
                month=date.today().month)
        except ObjectDoesNotExist:
            this_month = False

        cache.set('this_month', this_month)

    return {'this_month': cache.get('this_month')}
