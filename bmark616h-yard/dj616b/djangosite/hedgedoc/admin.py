from django.contrib import admin
from django import forms
from django.utils.html import format_html

from . import models


class NotesAdminForm(forms.ModelForm):

    class Meta:
        model = models.Notes
        # fields = "__all__"
        fields = [
        "id",
        "idn",
        "title",
        "content",
        "shortid",
        "createdat",
        "updatedat",
        #"viewcount",
        #"permission",
        # "authorship",
        #"deletedat",
        # "lastchangeat",
        # "lastchangeuserid",
        # "permission",
        # "savedat",
        ]

class NotesAdmin(admin.ModelAdmin):

    actions = None
    form = NotesAdminForm
    ordering = ['-createdat']
    list_display = [
        "idn",
        "slink",
        "title",
        "content_tr",
        # "show_pub_url",
        "updatedat",
        "id",
        # "createdat",
        # "alias",
        # "authorship",
        # "viewcount",
        # "permission",
    ]
    readonly_fields = [
        
        "idn",
        "id",
        "shortid",
        "createdat",
        "updatedat",
        # "permission",
        # "authorship",
        # "lastchangeat",
        # "lastchangeuserid",
        # "savedat",
        # "viewcount",
        # "deletedat",
        # "content",
        # "alias",
        # "lastchangedat",
        # "lastchangeuserid",
        # "content",
        # "title",
    ]
    list_display_links = [
        "id",
        "idn",
        "title",
        "updatedat",
        # "content",
        # "created_at",
    ]
    search_fields = [
        "id",
        "title",
        "content",
        "shortid",
    ]

    # https://stackoverflow.com/questions/1949248/how-to-add-clickable-links-to-a-field-in-django-admin
    def slink(self, obj):
        return format_html("<a href='https://hedge.198.144.183.160.nip.io/s/{url}'  target='_blank'>Link..</a>", url=obj.shortid)

    @admin.display()
    def content_tr(self, obj):
        return ("%s" % (obj.content))[0:80]

admin.site.register(models.Notes, NotesAdmin)
