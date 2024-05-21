from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from products.models import Deposit, Saving
from products.serializers import DepositSerializer, SavingSerializer
from articles.models import Article
from articles.serializers import ArticleSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposits(request, pk):
    deposits = Deposit.objects.filter(user=pk)
    serialiers = DepositSerializer(deposits, many=True)
    return Response(serialiers.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def savings(request, pk):
    savings = Saving.objects.filter(user=pk)
    serialiers = SavingSerializer(savings, many=True)
    return Response(serialiers.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articles(request, pk):
    articles = Article.objects.filter(user=pk)
    serialiers = ArticleSerializer(articles, many=True)
    return Response(serialiers.data)