from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('', views.home),
]
