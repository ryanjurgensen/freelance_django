from django.contrib import admin
from .models import *

class PortfolioItemAdmin(admin.ModelAdmin):
    sortable_field_name = "position"

    exclude = ('position',)

    class Media:
        js = (
            'js/admin_list_reorder.js',
        )
    
    list_display = ('title','position',)   # Don't forget to add the other fields that should be displayed in the list view here
    list_editable = ('position',)  # 'position' is the name of the model field which holds the position 

admin.site.register(PortfolioItem, PortfolioItemAdmin)
