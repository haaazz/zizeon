from django.urls import path
from . import views

app_name = 'currencies'
urlpatterns = [
    path('get_data/', views.get_data),
    path('exchange/', views.exchange),
]
