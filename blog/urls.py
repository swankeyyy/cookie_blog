from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('', views.home),
]
