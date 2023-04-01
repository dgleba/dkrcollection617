from django.contrib import admin
from django import forms
import re

from . import models


class bookmkAdminForm(forms.ModelForm):

    class Meta:
        model = models.bookmk
        fields = "__all__"


class bookmkAdmin(admin.ModelAdmin):
    actions = None
    form = bookmkAdminForm
    list_display = [
        "id",
        "short_title",
        "short_url",
        "short_body",
        "tagtext",
        "created_at",
        # "updated_at",
    ]

    @admin.display(description='UpperTitle')
    def upper_title(self, obj):
        return ("%s" % (obj.title)).upper()

    @admin.display()
    def short_title(self, obj):
        return ("%s" % (obj.title))[0:80]


    @admin.display(description='Shortened-URL')
    def short_url(self, obj):
        short = ("%s" % (obj.url))[0:80]
        clean = re.sub(r"""
                    [,.;@#?!&$-/\W_]+  # Accept one or more copies of punctuation
                    \ *           # plus zero or more copies of a space,
                    """,
                    " ",          # and replace it with a single space
                    short, flags=re.VERBOSE)
        return clean

    def short_body(self, obj):
        if not obj.body:
            return ""
        else:
            return obj.body[0:80]

    list_display_links = [
        "id",
        "short_title",
        "short_body",
        "created_at",
        # "updated_at",
    ]

    exclude = ('description',)

    readonly_fields = [
        "bhash",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "url",
        "title",
        "body",
        "tagtext",
        'id',
        "comment",
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(bookmkAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['title'].widget.attrs['style'] = 'width: 81%'
        form.base_fields['tagtext'].widget.attrs['style'] = 'width: 81%'
        return form

    # https://stackoverflow.com/questions/910169/resize-fields-in-django-admin
    # class YourModelAdmin(admin.ModelAdmin):
    #     formfield_overrides = {
    #         models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #         models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    #     }

    class Media:
        css = { "all": ("mark616/first.css",) }
        js = ("mark616/autosize.js",)
        
admin.site.register(models.bookmk, bookmkAdmin)


