from django.contrib import admin
from django import forms

from . import models


class NotesAdminForm(forms.ModelForm):

    class Meta:
        model = models.Notes
        fields = "__all__"


class NotesAdmin(admin.ModelAdmin):
    form = NotesAdminForm
    list_display = [
        "viewcount",
        "permission",
        "title",
        "alias",
        "shortid",
        "content",
        "authorship",
        "id",
    ]
    readonly_fields = [
        "viewcount",
        "permission",
        "title",
        "alias",
        "shortid",
        "content",
        "authorship",
        "id",
    ]


admin.site.register(models.Notes, NotesAdmin)
