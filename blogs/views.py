from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from . import models
from home.models import BreadImages

# Create your views here.
def blogs_list(request):
    # Get published blogs ordered by date
    blogs = models.Blog.objects.filter(status='published').select_related('author').order_by('-date')
    
    # Add pagination (6 blogs per page)
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get breadcrumb images
    try:
        breadcrumb_images = BreadImages.objects.first()
    except BreadImages.DoesNotExist:
        breadcrumb_images = None
    
    context = {
        'blogs': page_obj,
        'breadcrumb_images': breadcrumb_images,
        'total_blogs': paginator.count,
    }
    return render(request,'blogs_list.html', context)


def blogs_detail(request,slug):
    blog = get_object_or_404(models.Blog.objects.select_related('author').prefetch_related('components'),slug=slug)
    
    # Get related blogs (exclude current blog)
    related_blogs = models.Blog.objects.filter(status='published').exclude(slug=slug).select_related('author')[:3]
    
    context = {
        'blog': blog,
        'related_blogs': related_blogs,
    }
    return render(request,'blog_detail.html', context)