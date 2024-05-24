from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    # path('get_deposist/', views.get_deposit),
    path('deposit/', views.deposit),
    path('deposit/<int:pk>/', views.deposit_detail),
    path('deposit/<int:pk>/open/', views.open_deposit),
    path('deposit/<int:deposit_pk>/delete/', views.cancel_deposit),
    path('deposit/recommend/', views.deposit_recommend),
    # path('get_saving/', views.get_saving),
    path('saving/', views.saving),
    path('saving/<int:pk>/', views.saving_detail),
    path('saving/<int:pk>/open/', views.open_saving),
    path('saving/<int:saving_pk>/delete/', views.cancel_saving),
    path('saving/recommend/', views.saving_recommend),
]