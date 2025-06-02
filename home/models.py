from django.db import models

# Create your models here.

class SiteSettings(models.Model):

    business_name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    social_facebook = models.URLField(blank=True, null= True)
    social_instagram = models.URLField(blank=True, null= True)
    social_twitter = models.URLField(blank=True, null= True)
    social_youtube = models.URLField(blank=True, null= True)


    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"


class HomePageContent(models.Model):
    hero_title  = models.CharField(max_length=255)
    hero_subtitle  = models.TextField()
    featured_tours_title  = models.CharField(max_length=255)
    featured_tours_subtitle  = models.TextField()
    featured_activities_title  = models.CharField(max_length=255)
    featured_activities_subtitle  = models.TextField()
    blog_section_title = models.CharField(max_length=255)
    blog_section_subtitle  = models.TextField()
    testimonial_title = models.CharField(max_length=255)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Home Page Content"
    

class AboutUsContent(models.Model):
    # cover_image
    cover_image_title = models.CharField(max_length=255)
    about_us_title = models.CharField(max_length=255)
    about_us_description = models.TextField()
    # about_us_image
    company_statistics_title = models.CharField(max_length=255)
    testimonial_title = models.CharField(max_length=255)
    testimonial_description = models.TextField()
    team_title = models.CharField(max_length=255)

    updated_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Us Content"
    

class Testimonial(models.Model):
    message  = models.TextField()
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    profile_image =  models.ImageField(blank=True,null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "Testimonial"


class BrandNarrative(models.Model):
    # image
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Brand Narrative"
    
class Team(models.Model):
    # image
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    social_facebook = models.URLField(blank=True, null= True)
    social_instagram = models.URLField(blank=True, null= True)
    social_twitter = models.URLField(blank=True, null= True)
    social_linkedin = models.URLField(blank=True, null= True)

    def __str__(self):
        return "Team"
    
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

