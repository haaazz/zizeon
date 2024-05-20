from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('get_deposit/', views.get_deposit_data),
    path('see_deposit/', views.see_deposit_data),
    path('get_saving/', views.get_saving_data),
    # path('see_saving/', views.see_saving_data),
]
