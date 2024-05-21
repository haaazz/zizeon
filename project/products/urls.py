from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    # path('get_deposist/', views.get_deposit),
    path('deposit/', views.deposit),
    path('deposit/<int:pk>/', views.deposit_detail),
    path('deposit/<int:pk>/open/', views.open_deposit),
    # path('get_saving/', views.get_saving),
    path('saving/', views.saving),
    path('saving/<int:pk>/', views.saving_detail),
    path('saving/<int:pk>/open/', views.open_saving),
]
