from . import views
from django.urls import path

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contacts'),
    path('feedback/', views.CreateContact.as_view(), name='feedback')
]
