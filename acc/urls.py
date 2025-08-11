from django.urls import path
from acc import views

urlpatterns = [
    path('',views.mail, name='mail'),
]