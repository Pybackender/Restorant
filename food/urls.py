"""
URL configuration for food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from about.views import aboutView
from contactus.views import contactusView
from food import settings
from account.views import accountView
from django.conf.urls.static import static
from menu.views import menuView
from reservation.views import reservationView
from services.views import servicetView
from team.views import teamView
from testimonial.views import TestimonialView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accountView, name = "account" ),
    path('index.html', accountView, name = "account" ),
    path('about.html', aboutView, name = "about" ),
    path('service.html', servicetView, name = "service" ),
    path('menu.html', menuView, name = "menu" ),
    path('booking.html', reservationView, name = "reservation" ),
    path('team.html', teamView, name = "our team" ),
    path('testimonial.html', TestimonialView, name = "Testimonial" ),
    path('contact.html', contactusView, name = "contact" ),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, 
                          document_root=settings.STATIC_ROOT)