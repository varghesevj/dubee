from django.contrib import admin
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name',)


class PostComponentInline(admin.StackedInline):
    model = models.PostComponent
    extra = 1

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','author')
    prepopulated_fields = {'slug': ('title',)}

    inlines = [
        PostComponentInline,
    ]