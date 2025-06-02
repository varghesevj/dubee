from django.shortcuts import render,get_object_or_404
from . import models

# Create your views here.
def blogs_list(request):
    return render(request,'blogs_list.html')


def blogs_detail(request,slug):
    blog = get_object_or_404(models.Blog.objects.select_related('author').prefetch_related('components'),slug=slug)
    return render(request,'blog_detail.html',{'blog':blog})