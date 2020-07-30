from django.urls import path
from zipQT import views

urlpatterns = [
    path('', views.home, name='zipQT-home'),
    path('convert', views.convert, name='zipQT-convert'),
    path('help', views.help, name='zipQT-help'),
] 