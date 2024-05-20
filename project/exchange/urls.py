from django.urls import path
from . import views

app_name = 'exchange'
urlpatterns = [
    path('get_data/', views.get_data),
    path('', views.exchange),
]
