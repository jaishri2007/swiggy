from django.urls import path
from . import views
urlpatterns = [
    path('', views.swiggy),
    path('swiggy2/', views.swiggy2, name='swiggy2'),
]