from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from datetime import date
from search import views as search_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from months.views import MonthViewSet, list_months, month_view
from articles.views import author_view, subscribe
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'month', MonthViewSet)


urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^author/(?P<slug>.+?)/$', author_view, name='author'),

    url(r'^month/now/$', month_view, name='this_month', kwargs={
        'year': date.today().year,
        'month': date.today().month,
    }),
    url(r'^month/all/$', list_months, name='list_months'),
    url(r'^month/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', month_view, name='month'),

    url(r'^subscribe/$', subscribe, name='subscribe'),
    
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
