from django.shortcuts import render
from . import models
from packages.models import Package
from blogs.models import Blog
from django.http import JsonResponse

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