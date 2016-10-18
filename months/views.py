from django.shortcuts import render, get_object_or_404
from datetime import date
from months.models import Month
from articles.models import Article
from rest_framework import serializers, viewsets
from django.db.models import Q


class MonthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Month
        fields = ('theme', 'string_date')


class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer


def list_months(request):
    months = Month.objects.filter(
        Q(year__lt=date.today().year) |
        Q(year=date.today().year,
            month__lte=date.today().month))

    context = {'months': months}
    return render(request, "months/all_months.html", context)


def month_view(request, year, month):
    month = get_object_or_404(Month, month=month)
    articles = Article.objects.live().filter(theme=month)

    context = {
        'month': month,
        'articles': articles
    }
    return render(request, "months/view_month.html", context)
