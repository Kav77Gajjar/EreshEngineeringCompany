from django.urls import path
from . import views

urlpatterns = [
    path('', views.mail, name='mail'),
    path('blog/', views.blog_short, name='blog_short'),
    path('detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('services/', views.service_view, name='services'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
]