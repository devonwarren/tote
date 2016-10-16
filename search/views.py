from __future__ import absolute_import, unicode_literals
from datetime import date
from itertools import chain

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.db.models import Q

from wagtail.wagtailcore.models import Page
from articles.models import Article
from wagtail.wagtailsearch.models import Query
from months.models import Month
# from articles.models import Contributor


def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        # Combine all the model types
        pages = Article.objects.live().search(search_query)
        # contributors = Contributor.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
        months = Month.objects.filter(
            Q(theme__icontains=search_query, year__lt=date.today().year) |
            Q(theme__icontains=search_query, year=date.today().year,
                month__lte=date.today().month))

        search_results = list(chain(pages, months))
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
