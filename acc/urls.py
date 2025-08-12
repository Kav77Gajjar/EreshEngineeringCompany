from django.urls import path
from . import views

urlpatterns = [
    path('',views.mail, name='mail'),
    path('blog/', views.blog_short, name ='blog_short'),
]