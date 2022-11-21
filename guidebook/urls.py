"""guidebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404

urlpatterns = [
    path('checkout/', include('checkout.urls')),
    path('contact/', include('contact.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('guide.urls'), name='guide_urls'),
    path('accounts/', include('allauth.urls')),
    
]
