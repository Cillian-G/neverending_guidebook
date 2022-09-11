from . import views
from django.urls import path


urlpatterns = [
    path('', views.PreviewList.as_view(), name='home'),
    path('directory/', views.LocationList.as_view(), name='directory'),
    path('<slug:slug>/', views.LocationDetails.as_view(), name='location'),
    
]