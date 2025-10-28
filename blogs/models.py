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
        return self.title
    
    @property
    def short_intro(self):
        """Return a truncated version of intro for cards"""
        if len(self.intro) > 150:
            return self.intro[:150] + "..."
        return self.intro
    
    def get_reading_time(self):
        """Estimate reading time based on word count"""
        word_count = len(self.intro.split())
        for component in self.components.all():
            if component.paragraph:
                word_count += len(component.paragraph.split())
        
        # Average reading speed is 200 words per minute
        reading_time = max(1, word_count // 200)
        return f"{reading_time} Min{'s' if reading_time > 1 else ''} read"
    
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

    def save(self, *args, **kwargs):
        if not self.order:
            last_component = PostComponent.objects.filter(post=self.post).order_by('-order').first()
            if last_component:
                self.order = last_component.order + 1
            else:
                self.order = 1
        super(PostComponent, self).save(*args, **kwargs)

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
