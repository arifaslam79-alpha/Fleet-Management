from django.urls import path, include
from . import views

app_name = "fleets_management"

urlpatterns = [
     path('', views.home, name="Home"),
     path('about-us', views.about, name="About"),
     path('contact-us', views.contact, name="Contact"),
     path('contact-form', views.contact_form, name="Contact Form"),
     path('vehicle-register', views.vehicle_reg, name="Vehicle Register Form"),
     path('vehicle-tracking', views.vehicle_track, name="Vehicle Tracking"),
     path('driver-training', views.driver_training, name="Driver Training"),
]