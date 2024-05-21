from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import OpenDeposit, OpenSaving
from .serializers import OpenDepositSerializer, OpenSavingSerializer
from articles.models import Article
from articles.serializers import ArticleSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposits(request):
    deposits = OpenDeposit.objects.filter(user=request.user)
    serialiers = OpenDepositSerializer(deposits, many=True)
    return Response(serialiers.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def savings(request):
    savings = OpenSaving.objects.filter(user=request.user)
    serialiers = OpenSavingSerializer(savings, many=True)
    return Response(serialiers.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articles(request):
    articles = Article.objects.filter(user=request.user)
    serialiers = ArticleSerializer(articles, many=True)
    return Response(serialiers.data)