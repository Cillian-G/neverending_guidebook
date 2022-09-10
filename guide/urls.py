from . import views
from django.urls import path


urlpatterns = [
    path('', views.PreviewList.as_view(), name='home')
]