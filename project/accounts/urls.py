from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('products/', views.products),
    path('articles/', views.articles),
    path('recommend/', views.recommend),
    path('update/', views.update),
]