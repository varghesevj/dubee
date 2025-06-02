from home.models import SiteSettings

def site_settings(request):
    site_settings = SiteSettings.objects.first()
    return{
        'site_settings' : site_settings
    }