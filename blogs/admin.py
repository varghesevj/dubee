from django.contrib import admin
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PostComponentInline(admin.StackedInline):
    model = models.PostComponent
    extra = 1
    fields = ('section_type', 'heading', 'paragraph', 'single_image', 'order')


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'date')
    list_filter = ('status', 'date', 'author')
    search_fields = ('title', 'intro')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)
    ordering = ('-date',)

    inlines = [
        PostComponentInline,
    ]