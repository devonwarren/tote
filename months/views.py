from django.shortcuts import render
from months.models import Month
from rest_framework import serializers, viewsets


class MonthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Month
        fields = ('theme', 'string_date')


class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer


def list_months(request):
    months = Month.objects.all()
    context = {'months': months}
    render(request, "all_months.html", context)
