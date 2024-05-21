from django.shortcuts import render
from django.conf import settings
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CurrencySerializer
from .models import Currency

# Create your views here.
@api_view(['GET'])
def get_data(request):
    api_key = settings.EXC_KEY
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': api_key,
        'searchdate': '20240520',
        'data': 'AP01',
    }
    response = requests.get(url, params=params).json()
    
    for exchange in response:
        data = {
            'cur_unit': exchange.get('cur_unit'),
            'cur_nm': exchange.get('cur_nm'),
            'ttb': exchange.get('ttb'),
            'tts': exchange.get('tts'),
            'deal_bas_r': exchange.get('deal_bas_r'),
            'bkpr': exchange.get('bkpr'),
        }
        serializer = CurrencySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return Response({ 'message': 'saved!' })

@api_view(['GET'])
def exchange(request):
    currencies = Currency.objects.all() 
    serializers = CurrencySerializer(currencies, many=True)
    return Response(serializers.data)