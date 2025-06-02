from django.contrib import admin
from . import models

# Register your models here.
class HighlightInline(admin.StackedInline):
    model = models.Highlight
    extra = 1

class InclusionInline(admin.StackedInline):
    model = models.Inclusion
    extra = 1

class ExclusionInline(admin.StackedInline):
    model = models.Exclusion
    extra = 1

class ItineraryInline(admin.StackedInline):
    model = models.Itinerary
    extra = 1

class FAQInline(admin.StackedInline):
    model = models.FAQ
    extra =1

class ImageGalleryInline(admin.StackedInline):
    model=models.ImageGallery
    extra = 1

@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'category', 'price')
    search_fields = ('title', 'location')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}

    inlines = [
        ImageGalleryInline,
        HighlightInline,
        InclusionInline,
        ExclusionInline,
        ItineraryInline,
        FAQInline,
    ]

@admin.register(models.Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display=("name","email","submitted_at","package")
    readonly_fields= ("package",)

@admin.register(models.Booking)
class BoookingAdmin(admin.ModelAdmin):
    list_display= ("name","email","created_at","date","package")
    readonly_fields= ("package",)
