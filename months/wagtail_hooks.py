from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Month


class MonthsAdmin(ModelAdmin):
    model = Month
    menu_icon = 'date'
    menu_order = 200
    add_to_settings_menu = False
    list_display = ('theme', 'year', 'month')
    list_filter = ('year', )
    search_fields = ('theme', )

modeladmin_register(MonthsAdmin)
