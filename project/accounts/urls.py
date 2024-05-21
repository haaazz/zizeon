from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:pk>/deposits/', views.deposits),
    path('<int:pk>/savings/', views.savings),
    path('<int:pk>/articles/', views.articles),
]
