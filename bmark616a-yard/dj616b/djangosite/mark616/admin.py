from django.contrib import admin
from django import forms

from . import models


class bookmkAdminForm(forms.ModelForm):

    class Meta:
        model = models.bookmk
        fields = "__all__"


class bookmkAdmin(admin.ModelAdmin):
    form = bookmkAdminForm
    list_display = [
        "bhash",
        "description",
        "comment",
        "url",
        "title",
        "created_at",
        "updated_at",
    ]
    readonly_fields = [
        "bhash",
        "description",
        "comment",
        "url",
        "title",
        "created_at",
        "updated_at",
    ]


admin.site.register(models.bookmk, bookmkAdmin)
