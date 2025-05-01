from django.contrib import admin
from .models import Products,Order

admin.site.site_header="E-Commerce Site"
admin.site.site_title="ABC Shopping"
admin.site.index_title="Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description="Default Category"
    list_display=('title','price','discount_price','category','description','image')
    search_fields=('title','category')
    actions=('change_category_to_default',)
    fields=('title','price',)
    list_editable=('price','discount_price',)
# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)

