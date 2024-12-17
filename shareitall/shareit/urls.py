from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('add-listing/', views.add_listing, name='add_listing'),
    path('add-service/', views.add_service, name='add_service'),
    path('forum/', views.forum, name='forum'),

    path('listing-success/', views.listing_success, name='listing_success'),
    path('listing/<int:id>/', views.listing_detail, name='listing_detail'),
    path('about/', views.about_us, name='about_us'),  # About Us page
    path('contact/', views.contact_us, name='contact_us'),  # Contact Us page
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

    path('view_services/', views.view_services, name='view_services'),
    path('current_listings/', views.current_listings, name='current_listings'),
    path('view_services/', views.view_services, name='view_services'),
    path('ongoing_discussions/<int:pk>/', views.ongoing_discussions, name='ongoing_discussions'),
    path('ongoing_discussions/', views.ongoing_discussions, name='ongoing_discussions'),
    path('forum/<int:pk>/', views.forum_detail, name='forum_detail'),

    path('donation_form/', views.donation_form, name='donation_form'),
    path('api/mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),
    path('current_donations/', views.current_donations, name='current_donations'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)