from django.shortcuts import render

# Create your views here.
# def tours_list(request):
#     return render(request, 'packagelist.html')


def tours_list(request):
    return render(request, 'package_list.html', {
        'category': 'Tours'
    })

def activities_list(request):
    return render(request, 'package_list.html', {
        'category': 'Activities'
    })

def package_detail(request, category, id):
    return render(request, 'package_details.html', {
        'category': category.capitalize(),  # "Tours" or "Activities"
        'id': id
    })