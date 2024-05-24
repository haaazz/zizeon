from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment
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
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        if article.user != request.user:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        elif request.method == 'DELETE':
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

@api_view(['GET', 'POST'])
def comments(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(article=article)
        serializers = CommentSerializer(comments, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def comments_detail(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        if request.user != comment.user:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        elif request.method == 'DELETE':
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)