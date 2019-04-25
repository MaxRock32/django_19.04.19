from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('contacti/', views.contacti, name="blog-contacti"),
]