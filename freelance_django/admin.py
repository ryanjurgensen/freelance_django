from django.contrib import admin
from .models import *

class PortfolioItemAdmin(admin.ModelAdmin):
    sortable_field_name = "position"
    raw_id_fields = ('tags',)
    search_fields = ['title',]

    autocomplete_lookup_fields = {
        'm2m': ['tags'],
    }

    exclude = ('position',)

    class Media:
        js = (
            'js/admin_list_reorder.js',
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        )
    
    list_display = ('title','position',)   # Don't forget to add the other fields that should be displayed in the list view here
    list_editable = ('position',)  # 'position' is the name of the model field which holds the position 

admin.site.register(PortfolioTag)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
