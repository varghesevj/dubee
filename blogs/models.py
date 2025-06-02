from django.db import models
import os


def image_upload_to(instance, filename):
    # If instance is Blog, use its slug
    if hasattr(instance, 'slug'):
        slug = instance.slug
    # If instance has a 'post' FK (like PostComponent), get post.slug
    elif hasattr(instance, 'post') and hasattr(instance.post, 'slug'):
        slug = instance.post.slug
    else:
        slug = 'misc_blogs'
    return os.path.join('blogs', slug, filename)


# def image_upload_to(instance,filename):
#     blog_slug = instance.post.slug if instance.post else 'misc_blogs'
#     return os.path.join('blogs',blog_slug,filename)

class Blog(models.Model):

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to=image_upload_to,null=True,blank=True)
    author = models.ForeignKey('Author',on_delete=models.CASCADE,related_name="author",null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    intro = models.TextField()
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices= STATUS_CHOICES,default= 'draft')


    def __str__(self):
        return "Blog"
    
class PostComponent(models.Model):
    component_type = [
        ('heading', 'Heading'),
        ('paragraph','Paragraph'),
        ('single_image','Single Image'),
        ('image_gallery','Image Gallery')
    ]
    post = models.ForeignKey('Blog',related_name='components',on_delete=models.CASCADE)
    section_type = models.CharField(max_length=20,choices=component_type)
    heading = models.CharField(max_length=255,null=True,blank=True)
    paragraph = models.TextField(blank=True,null=True)
    single_image = models.ImageField(upload_to=image_upload_to,null=True,blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.section_type} - {self.order}"

    


class Author(models.Model):
    profile_image = models.ImageField(upload_to='authors/',null=True,blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    social_facebook = models.URLField(blank=True, null= True)
    social_instagram = models.URLField(blank=True, null= True)
    social_twitter = models.URLField(blank=True, null= True)
    social_linkedin = models.URLField(blank=True,null=True)

    def __str__(self):
        return  self.name
