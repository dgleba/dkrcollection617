from django.contrib import admin
from django import forms

from . import models


class bookmkAdminForm(forms.ModelForm):

    class Meta:
        model = models.bookmk
        fields = "__all__"


class bookmkAdmin(admin.ModelAdmin):
    form = bookmkAdminForm
    list_display = list_display_links = [
        "id",
        "comment",
        "url",
        "title",
        "created_at",
        "updated_at",
    ]
    readonly_fields = [
        "bhash",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "title",
        "description",
        'id',
        "comment",
        "url",
    ]


admin.site.register(models.bookmk, bookmkAdmin)
