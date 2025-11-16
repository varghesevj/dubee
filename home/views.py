from django.shortcuts import render
from . import models
from packages.models import Package
from blogs.models import Blog
from django.http import JsonResponse



# cloudinary debug

# home/views.py
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def cloudinary_test(request):
    # Show what storage is being used
    storage_class = default_storage.__class__.__name__

    # Try to upload a dummy file
    test_file_name = "test_upload.txt"
    test_content = ContentFile(b"This is a test file for Cloudinary")
    
    if default_storage.exists(test_file_name):
        default_storage.delete(test_file_name)
    
    file_name = default_storage.save(test_file_name, test_content)
    file_url = default_storage.url(file_name)

    response_text = (
        f"Storage class: {storage_class}\n"
        f"File saved as: {file_name}\n"
        f"File URL: {file_url}\n"
    )

    return HttpResponse(response_text, content_type="text/plain")






# Create your views here.
def home_page(request):
    featured_tours = Package.objects.filter(category = 'tour',is_featured=True)[:6]
    featured_activities = Package.objects.filter(category = 'activity',is_featured=True)[:6]
    
    # Get latest published blogs for homepage
    featured_blogs = Blog.objects.filter(status='published').select_related('author').order_by('-date')[:3]
    
    # Get homepage content with fallback
    try:
        homepage_content = models.HomePageContent.objects.first()
    except models.HomePageContent.DoesNotExist:
        homepage_content = None

    context = {
        'homepage_content': homepage_content,
        'featured_tours': featured_tours,
        'featured_activities': featured_activities,
        'featured_blogs': featured_blogs,
        'testimonials': models.Testimonial.objects.filter(is_active=True),
    }

    return render(request,'home.html',context)

def about_page(request):
    return render(request,'about.html',{
        'aboutuscontent':models.AboutUsContent.objects.first(),
        'brand_narratives' : models.BrandNarrative.objects.filter(is_active=True),
        'teams': models.Team.objects.filter(is_active=True),
        'testimonials': models.Testimonial.objects.filter(is_active=True),
                                        
    })

def contact_page(request):
    return render(request,'contact.html')


def subscribe_newsletter(request):
    print("VIEW HIIIIIIIIIIIIT!")  # Debug
    if request.method== "POST":
        email = request.POST.get('email')
        print("Email received:", email)  # Debug
        if email:
            obj, created = models.NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                return JsonResponse({'success': True, 'message': 'Subscribed successfully!'})
            else:
                return JsonResponse({'success': False, 'message': 'Email already subscribed.'})
        else:
            return JsonResponse({'success': False, 'message': 'Email is required.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})


def send_message(request):
    print("hittttttttttt")
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     message =request.POST.get('message')

    #     models.Messages.objects.create(
    #         name = name,
    #         email =email,
    #         message = message
    #     )
        
    #     return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
    # return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            models.Messages.objects.create(
                name=name,
                email=email,
                message=message
            )

            return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)