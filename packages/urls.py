from django.urls import path
from .views import tours_list,activities_list,package_detail,enquiry_view,submit_booking
# from .views import activities_list

# urlpatterns = [
#     path('tours/',tours_list, name='tours_list'),  # Render the packagelist.html template for tours

    
# ]

urlpatterns = [
    path('tours/',tours_list, name='tours_list'),
    path('activities/', activities_list, name='activities_list'),
    # path('<str:category>/<int:id>/', package_detail, name='package_detail'),  # dynamic detail page
    path('<str:category>/<slug:slug>/enquiry/', enquiry_view, name='enquiry'),
    
    path('<str:category>/<slug:slug>/', package_detail, name='package_detail'),
    # path('enquiry/', enquiry_view, name='enquiry'),
    # path('<category>/<slug>/enquiry/', enquiry_view, name='enquiry'),
    path('submit-booking/', submit_booking, name='submit_booking'),

]