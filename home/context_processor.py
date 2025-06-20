from home.models import SiteSettings,BreadImages,Miscellaneous

def site_settings(request):
    site_settings = SiteSettings.objects.first()
    breadcrumb_images = BreadImages.objects.first()
    miscellaneous = Miscellaneous.objects.first()
    return{
        'site_settings' : site_settings,
        'breadcrumb_images' : breadcrumb_images,
        'miscellaneous' : miscellaneous
    }

