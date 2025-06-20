from django.db import models
from django.utils.text import slugify
import os


def package_image_upload_path(instance, filename):
    return os.path.join('packages', instance.slug, filename)

def image_gallery_upload_path(instance,filename):
    return os.path.join('packages', instance.package.slug,'gallery' ,filename)


def image_itinerary_upload_path(instance,filename):
    return os.path.join('packages', instance.package.slug,'itinerary-images' ,filename)
# Create your models here.
class Package(models.Model):
    category_choices = [
        ('tour','Tour'),
        ('activity','Activity')
    ]
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category =models.CharField(max_length=20,choices=category_choices)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    group_size = models.IntegerField()
    package_type = models.CharField(max_length=100)
    min_age = models.IntegerField()
    pickup_location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured =models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to=package_image_upload_path, null=True, blank=True)
    video = models.URLField(blank=True,null=True)
    map_embed_code = models.TextField(
        blank=True,
        help_text="Paste the full Google Maps iframe embed code here"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def save_percentage(self):
        if self.old_price and self.old_price > self.price:
            return round((self.old_price - self.price) / self.old_price * 100)
        return 0

    def __str__(self):
        return self.title
    
class ImageGallery(models.Model):
    package = models.ForeignKey(Package, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_gallery_upload_path)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.package.title}"

    

class Highlight(models.Model):
    package = models.ForeignKey('Package', related_name='highlights', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    
class Inclusion(models.Model):
    package = models.ForeignKey('Package', related_name='inclusions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    
class Exclusion(models.Model):
    package = models.ForeignKey('Package', related_name='exclusions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    

class Itinerary(models.Model):
    package = models.ForeignKey('Package', related_name='itineraries', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=image_itinerary_upload_path,blank=True,null=True)

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    package = models.ForeignKey('Package', related_name='faqs', on_delete=models.CASCADE)
    faq_question = models.TextField()
    faq_answer =models.TextField()

    def __str__(self):
        return self.faq_question
    
class Enquiry(models.Model):
    package = models.ForeignKey('Package', related_name='Enquiry', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Booking(models.Model):
    package = models.ForeignKey('Package', related_name='Booking', on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    adults = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    infants = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.name} on {self.date}"