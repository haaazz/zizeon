from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # path('get_articles/', views.get_articles),
    # path('get_comments/', views.get_comments),
    path('', views.article),
    path('<int:pk>/', views.article_detail),
    path('<int:pk>/comments/', views.comments),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comments_detail),
]