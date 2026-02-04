from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tuna/', views.tuna, name='tuna'),
    path('coral/', views.coral, name='coral'),
    path('tbd/', views.tbd, name='tbd'),
]