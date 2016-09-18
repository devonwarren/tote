from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Contributor


class ContributorAdmin(ModelAdmin):
    model = Contributor
    menu_icon = 'edit'
    menu_order = 300
    add_to_settings_menu = False
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

modeladmin_register(ContributorAdmin)
