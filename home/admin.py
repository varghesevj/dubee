from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not models.SiteSettings.objects.exists()
    

    def has_delete_permission(self, request, obj = None):
        return False
    
    list_display = ('business_name', 'email', 'phone' )

@admin.register(models.HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not models.HomePageContent.objects.exists()
    

    def has_delete_permission(self, request, obj = None):
        return False
    
    def name(self,obj):
        return "Home Page Content"
    
    list_display = ('name','updated_at')

@admin.register(models.AboutUsContent)
class AboutUsContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not models.AboutUsContent.objects.exists()
    

    def has_delete_permission(self, request, obj = None):
        return False
    
    def name(self,obj):
        return "About Us Content"
    
    list_display = ('name','updated_at')


@admin.register(models.Testimonial)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'is_active')  
    list_filter = ('is_active',)          
    search_fields = ('name', 'location', 'message')   
    list_editable = ('is_active',)    

    def name(self,obj):
        return "Testimonial"

@admin.register(models.BrandNarrative)
class BrandNarrativeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','is_active')
    list_editable = ('is_active',)


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation','is_active')
    list_editable = ('is_active',)

@admin.register(models.NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display=('email','subscribed_at')
