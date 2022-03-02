from .models import *
from django.contrib import admin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'draft',)
    list_editable = ("draft",)
    list_filter = ('category', 'draft', )
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}

    actions = ['published', 'unpublished']

    save_on_top = True
    save_as = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Profile)
admin.site.register(CartItem)
