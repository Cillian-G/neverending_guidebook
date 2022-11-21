from . import views
from django.urls import path


urlpatterns = [
    path('', views.PreviewList.as_view(), name='home'),
    path('directory/', views.LocationList.as_view(), name='directory'),
    path('my_account/', views.my_account, name='my_account'),
    path('region/add/', views.add_region, name='add_region'),
    path('location/add/', views.add_location, name='add_location'),
    path(
        'location/edit/<int:location_id>',
        views.edit_location, name='edit_location'),
    path(
        'location/delete/<int:location_id>',
        views.delete_location, name='delete_location'),
    path('<slug:slug>/', views.LocationDetails.as_view(), name='location'),
    path(
        'bookmark/<slug:slug>/', views.LocationBookmark.as_view(),
        name='location_bookmark'
        ),
    path('region/delete/<item_id>', views.delete_region, name='delete_region'),
    path('region/edit/<item_id>', views.edit_region, name='edit_region'),
]
