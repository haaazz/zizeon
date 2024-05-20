from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticlesSerializer, CommentsSerializer
from random import randint

# Create your views here.
@api_view(['GET'])
def get_articles(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url).json()

    for article in response:
        data = {
            'user': article.get('userId'),
            'title': article.get('title'),
            'content': article.get('body'),
        }
        serializer = ArticlesSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return Response({ 'message': 'saved!' })

@api_view(['GET'])
def get_comments(request):
    url = 'https://jsonplaceholder.typicode.com/comments'
    response = requests.get(url).json()

    for comment in response:
        userId = randint(1, 99)
        data = {
            'user': userId,
            'article': comment.get('postId'),
            'content': comment.get('body'),
        }
        serializer = CommentsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return Response({ 'message': 'saved!' })

@api_view(['GET'])
def article(request):
    articles = Article.objects.all()
    serializers = ArticlesSerializer(articles, many=True)
    return Response(serializers.data)