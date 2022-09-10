from . import views
from django.urls import path


urlpatterns = [
    path('', views.PreviewList.as_view(), name='home'),
    path('<slug:slug>/', views.LocationDetails.as_view(), name='location')
]