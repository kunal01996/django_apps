from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogPageListView.as_view(), name='Blog Pages'),
    path('detail/<int:pk>/', views.BlogPageDetailView.as_view(), name='blog_page_detail')
]
