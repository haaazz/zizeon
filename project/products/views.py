from django.shortcuts import render
from django.conf import settings
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Deposit, DepositOption, Saving, SavingOption
from .serializers import DepositsSerializer, DepositOptionsSerializer, SavingsSerializer, SavingOptionsSerializer

# Create your views here.
@api_view(['GET'])
def get_deposit(request):
    api_key = settings.FIN_KEY
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(url, params=params).json().get('result')

    baselist = response.get('baseList')
    optionlist = response.get('optionList')

    for product in baselist:
        data = {
            'dcls_month' : product.get('dcls_month', '-'),
            'fin_co_no' : product.get('fin_co_no'),
            'kor_co_nm' : product.get('kor_co_nm', '-'),
            'fin_prdt_cd' : product.get('fin_prdt_cd'),
            'fin_prdt_nm' : product.get('fin_prdt_nm', '-'),
            'join_member' : product.get('join_member', '-'),
            'join_way' : product.get('join_way', '-'),
            'join_deny' : product.get('join_deny', -1),
            'etc_note' : product.get('etc_note', '-'),
            'spcl_cnd' : product.get('spcl_cnd', '-'),
            'mtrt_int' : product.get('mtrt_int', '-'),
        }
        serializer = DepositsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
    for option in optionlist:
        product = Deposit.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
        if product:
            data = {
                'deposit': product.id,
                'fin_prdt_cd': option.get('fin_prdt_cd'),
                'intr_rate_type_nm': option.get('intr_rate_type_nm', '-'),
                'intr_rate': option.get('intr_rate', -1),
                'intr_rate2': option.get('intr_rate2', -1),
                'save_trm': option.get('save_trm', '-')
            }
            serializer = DepositOptionsSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(deposit=product)

    return Response({ 'message': 'saved!' })

@api_view(['GET'])
def deposit(request):
    deposits = Deposit.objects.all()
    serializers = DepositsSerializer(deposits, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def get_saving(request):
    api_key = settings.FIN_KEY
    url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(url, params=params).json().get('result')
    baselist = response.get('baseList')
    optionlist = response.get('optionList')
    
    for product in baselist:
        data = {
            'dcls_month' : product.get('dcls_month', '-'),
            'fin_co_no' : product.get('fin_co_no'),
            'kor_co_nm' : product.get('kor_co_nm', '-'),
            'fin_prdt_cd' : product.get('fin_prdt_cd'),
            'fin_prdt_nm' : product.get('fin_prdt_nm', '-'),
            'join_member' : product.get('join_member', '-'),
            'join_way' : product.get('join_way', '-'),
            'join_deny' : product.get('join_deny', -1),
            'etc_note' : product.get('etc_note', '-'),
            'spcl_cnd' : product.get('spcl_cnd', '-'),
            'mtrt_int' : product.get('mtrt_int', '-'),
        }
        serializer = SavingsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
    for option in optionlist:
        product = Saving.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
        if product:
            data = {
                'saving': product.id,
                'fin_prdt_cd': option.get('fin_prdt_cd'),
                'intr_rate_type_nm': option.get('intr_rate_type_nm', '-'),
                'rsrv_type_nm': option.get('rsrv_type_nm', '-'),
                'intr_rate': option.get('intr_rate', -1),
                'intr_rate2': option.get('intr_rate2', -1),
                'save_trm': option.get('save_trm', '-')
            }
            serializer = SavingOptionsSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(saving=product)

    return Response({ 'message': 'saved!' })

@api_view(['GET'])
def saving(request):
    savings = Saving.objects.all()
    serializers = SavingsSerializer(savings, many=True)
    return Response(serializers.data)