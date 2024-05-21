from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('deposits/', views.deposits),
    path('savings/', views.savings),
    path('articles/', views.articles),
]
