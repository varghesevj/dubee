from django.core.management.base import BaseCommand
from blogs.models import Blog, Author, PostComponent
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Create sample blog data for testing'

    def handle(self, *args, **options):
        # Create sample author
        author, created = Author.objects.get_or_create(
            name="John Traveler",
            defaults={
                'description': "John is an experienced travel blogger who has visited over 50 countries and loves sharing his adventures and travel tips with fellow wanderers.",
                'social_facebook': "https://facebook.com/johntraveler",
                'social_instagram': "https://instagram.com/johntraveler",
                'social_twitter': "https://twitter.com/johntraveler",
            }
        )
        
        if created:
            self.stdout.write(f"Created author: {author.name}")
        
        # Create sample blogs
        sample_blogs = [
            {
                'title': 'Best Travel Destinations in 2024',
                'intro': 'Discover the most amazing travel destinations that you must visit in 2024. From exotic beaches to bustling cities, these places will leave you mesmerized.',
                'slug': 'best-travel-destinations-2024',
            },
            {
                'title': 'Budget Travel Tips for Backpackers',
                'intro': 'Learn how to travel the world on a budget with these essential tips for backpackers. Save money while experiencing amazing adventures.',
                'slug': 'budget-travel-tips-backpackers',
            },
            {
                'title': 'Hidden Gems in Southeast Asia',
                'intro': 'Explore the lesser-known but incredibly beautiful destinations in Southeast Asia that most tourists miss.',
                'slug': 'hidden-gems-southeast-asia',
            }
        ]
        
        for blog_data in sample_blogs:
            blog, created = Blog.objects.get_or_create(
                slug=blog_data['slug'],
                defaults={
                    'title': blog_data['title'],
                    'intro': blog_data['intro'],
                    'author': author,
                    'status': 'published',
                }
            )
            
            if created:
                self.stdout.write(f"Created blog: {blog.title}")
                
                # Add sample components
                PostComponent.objects.create(
                    post=blog,
                    section_type='heading',
                    heading='Introduction',
                    order=1
                )
                
                PostComponent.objects.create(
                    post=blog,
                    section_type='paragraph',
                    paragraph='This is a sample paragraph for the blog post. It contains detailed information about the topic and provides valuable insights for readers.',
                    order=2
                )
                
                PostComponent.objects.create(
                    post=blog,
                    section_type='heading',
                    heading='Key Points',
                    order=3
                )
                
                PostComponent.objects.create(
                    post=blog,
                    section_type='paragraph',
                    paragraph='Here are the key points you need to know about this topic. These insights will help you make better decisions and enhance your travel experience.',
                    order=4
                )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample blog data!')
        )