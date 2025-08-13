from django.contrib import admin
from django.urls import path, include
from acc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_short, name='home'),
    path('contact/', views.mail, name='mail'),
path("blog/", views.blog_list, name="blog_list"),
    path('', include('acc.urls')),  # Include app URLs
]
