from django.urls import path
from .views import home_page,about_page,contact_page,subscribe_newsletter,send_message

from .views import cloudinary_test

urlpatterns = [
    path('', home_page, name='home'),
    path('aboutus/', about_page, name='about'),
    # path('send_message/',send_message,name='send_message'),
    path('contactus/', contact_page, name='contact'),
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
    path('send_message/',send_message,name='send_message'),

    path('cloudinary-test/', cloudinary_test, name='cloudinary_test'),
]

