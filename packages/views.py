from django.shortcuts import render , get_object_or_404
from django.http import JsonResponse
from .models import Package,Booking
from .forms import EnquiryForm
from django.core.paginator import Paginator
# Create your views here.
# def tours_list(request):
#     return render(request, 'packagelist.html')


def paginate_packages(request, queryset, category_name,category_key):
    paginator = Paginator(queryset, 10)  # Show 6 packages per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'package_list.html', {
        'category': category_name,
        'packages': page_obj,  # This is now a page object
        'category_key': category_key, 
    })

def tours_list(request):
    tours = Package.objects.filter(category='tour')
    # return render(request, 'package_list.html', {
    #     'category': 'Tours',
    #     'packages' : tours,
    # })
    return paginate_packages(request, tours, 'Tours','tour')

def activities_list(request):
    activities = Package.objects.filter(category='activity')
    # return render(request, 'package_list.html', {
    #     'category': 'Activities',
    #     'packages': activities,
    # })
    return paginate_packages(request, activities, 'Activities','activity')

def package_detail(request, category, slug):
    package = get_object_or_404(Package, slug=slug, category=category.lower())
    highlights = list(package.highlights.all())
    mid = (len(highlights) + 1) // 2  
    highlights_col1 = highlights[:mid]
    highlights_col2 = highlights[mid:]
    related_packages = Package.objects.filter(category=category.lower()).exclude(id=package.id)[:3]


    return render(request, 'package_details.html', {
        'category': category.capitalize(),  # "Tours" or "Activities"
        'package': package,
        'highlights_col1': highlights_col1,
        'highlights_col2': highlights_col2,
        'related_packages': related_packages,
    })

def enquiry_view(request,category,slug):
    package = get_object_or_404(Package, category=category, slug=slug)
    success = False
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = EnquiryForm()
            print("doneeeeeeeeeeeeeeeeeeeeeeeee")
        else:
            print(form.errors)
    else:
        form = EnquiryForm()

    return render(request, 'package_details.html', {'form': form, 'success': success,'package': package })


def submit_booking(request):
    if request.method == 'POST':
        data = request.POST

        try:
            print(data.get('package_id'))
            package = Package.objects.get(id=data.get('package_id'))
        except Package.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid package selected.'})

        booking = Booking.objects.create(
            package=package,
            name=data.get('name'),
            email=data.get('email'),
            mobile=data.get('mobile'),
            message=data.get('message'),
            adults=int(data.get('adults', 0)),
            children=int(data.get('children', 0)),
            infants=int(data.get('infants', 0)),
            date=data.get('daterange'),
        )

        print(booking.message)

        # return JsonResponse({'status': 'success', 'message': 'Booking received!'})
    
        return JsonResponse({
            'status': 'success',
            'message': 'Booking received!',
            'booking': {
                'package': package.title,
                'name': booking.name,
                'email': booking.email,
                'mobile': booking.mobile,
                'date': booking.date,
                'adults': booking.adults,
                'children': booking.children,
                'infants': booking.infants,
                'message' : booking.message,
            }
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
