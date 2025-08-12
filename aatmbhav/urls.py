from django.contrib import admin
from django.urls import path
from acc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_short, name='home'),
    path('contact/', views.mail, name='mail'),
]
