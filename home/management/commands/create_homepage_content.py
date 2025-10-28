from django.core.management.base import BaseCommand
from home.models import HomePageContent


class Command(BaseCommand):
    help = 'Create default homepage content if it does not exist'

    def handle(self, *args, **options):
        if not HomePageContent.objects.exists():
            homepage_content = HomePageContent.objects.create(
                hero_title="Discover Amazing Destinations",
                hero_subtitle="Explore the world with our carefully curated tours and activities. Create unforgettable memories with Dubee.",
                featured_tours_title="Featured Tours",
                featured_tours_subtitle="Discover our most popular and exciting tour packages that will take you to amazing destinations around the world.",
                featured_activities_title="Featured Activities",
                featured_activities_subtitle="Experience thrilling activities and adventures that will make your trip unforgettable and exciting.",
                blog_section_title="Latest Travel Stories",
                blog_section_subtitle="Read inspiring travel stories, tips, and guides from our community of travelers and experts.",
                testimonial_title="What Our Customers Say"
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created homepage content!')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Homepage content already exists.')
            )