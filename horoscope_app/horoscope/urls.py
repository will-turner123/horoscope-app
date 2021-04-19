from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='horoscope-home'),
     path('about/', views.about, name='horoscope-about'),
     path('horoscope/<str:sign>/<str:timeframe>', views.horoscope, name='horoscope-horoscope')
]