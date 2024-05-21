from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer
from random import randint
from rest_framework import status

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
        serializer = ArticleSerializer(data=data)
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
        serializer = CommentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return Response({ 'message': 'saved!' })

@api_view(['GET', 'POST'])
def article(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        # serializer = ArticleSerializer(data=request.data)
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(user=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])   
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)