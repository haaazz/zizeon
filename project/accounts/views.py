from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import OpenDeposit, OpenSaving
from .serializers import OpenDepositSerializer, OpenSavingSerializer, UserSerialzer
from articles.models import Article
from articles.serializers import ArticleSerializer

# Create your views here.
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def products(request):
    deposits = OpenDeposit.objects.filter(user=request.user)
    savings = OpenSaving.objects.filter(user=request.user)
    deposit_serialiers = OpenDepositSerializer(deposits, many=True)
    saving_serialiers = OpenSavingSerializer(savings, many=True)
    return Response({'open_deposits': deposit_serialiers.data, 'open_savings': saving_serialiers.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articles(request):
    articles = Article.objects.filter(user=request.user)
    serialiers = ArticleSerializer(articles, many=True)
    return Response(serialiers.data)

import pandas as pd
import sqlite3
from sklearn.preprocessing import LabelEncoder

con = sqlite3.connect("db.sqlite3", check_same_thread=False)
le = LabelEncoder()
gender_list = {'Male': 1, 'Female': 2}
job_list = {
    'Analyst': 1,
    'Teacher': 2,
    'Lawyer': 3,
    'Researcher': 4,
    'Photographer': 5,
    'Manager': 6,
    'Writer': 7,
    'Designer': 8,
    'Doctor': 9,
    'Artist': 10,
    'Nurse': 11,
    'Chef': 12,
    'Student': 13,
    'Engineer': 14,
    'Marketer': 15,
    'Developer': 16,
    'Accountant': 17
}

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def recommend(request):
    user = pd.read_sql("SELECT * FROM accounts_user", con, index_col=None)
    user = user.drop(['password', 'last_login', 'is_superuser', 'is_staff', 'username', 'first_name', 'last_name', 'email', 'nickname', 'date_joined'], axis=1)
    opendeposit = pd.read_sql("SELECT * FROM accounts_opendeposit", con, index_col=None)
    opensaving = pd.read_sql("SELECT * FROM accounts_opensaving", con, index_col=None)
    deposits = pd.merge(opendeposit, user.rename(columns={'id': 'user_id'}), on='user_id')
    deposits = deposits.drop(['balance', 'id'], axis=1)
    deposits = deposits.drop(deposits[deposits['user_id'] == request.user.pk].index)
    savings = pd.merge(opensaving, user.rename(columns={'id': 'user_id'}), on='user_id')
    savings = savings.drop(['balance', 'id'], axis=1)
    savings = savings.drop(savings[savings['user_id'] == request.user.pk].index)

    deposit_target = deposits.deposit_id
    deposit_train = deposits.drop(['deposit_id', 'user_id'], axis=1)
    deposit_test = user[user['id'] == request.user.pk]
    deposit_test = deposit_test.drop('id', axis=1)
    saving_target = savings.saving_id
    saving_train = savings.drop(['saving_id', 'user_id'], axis=1)
    saving_test = user[user['id'] == request.user.pk]
    saving_test = saving_test.drop('id', axis=1)

    deposit_train['gender'] = le.fit_transform(deposit_train['gender'].values)
    deposit_train['job'] = le.fit_transform(deposit_train['job'].values)
    saving_train['gender'] = le.fit_transform(saving_train['gender'].values)
    saving_train['job'] = le.fit_transform(saving_train['job'].values)

    return Response({'test': deposit_train})

@api_view(['DELETE', 'PUT'])
# @permission_classes(IsAuthenticated)
def update(request):
    user = request.user
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print(user)
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'PUT':
        serialzer = UserSerialzer(user, data=request.data, partial=True)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save()
            return Response(status=status.HTTP_202_ACCEPTED)