from django.urls import path
from zipQT import views

urlpatterns = [
    path('', views.home, name='zipQT-home'),
    path('help', views.help, name='zipQT-help'),
    path('convert', views.convert, name='zipQT-convert'),
] 