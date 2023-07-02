from django.contrib import admin
from .models import Women, Category


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
