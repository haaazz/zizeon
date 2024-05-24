from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import OpenDeposit, OpenSaving
from .serializers import OpenDepositSerializer, OpenSavingSerializer, UserSerialzer
from articles.models import Article
from articles.serializers import ArticleSerializer
from products.models import Deposit, Saving
from products.serializers import DepositSerializer, SavingSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products(request):
    deposits = OpenDeposit.objects.filter(user=request.user)
    deposit_serializers = OpenDepositSerializer(deposits, many=True)
    savings = OpenSaving.objects.filter(user=request.user)
    saving_serializers = OpenSavingSerializer(savings, many=True)
    return Response({'deposits': deposit_serializers.data, 'savings': saving_serializers.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articles(request):
    articles = Article.objects.filter(user=request.user)
    serialiers = ArticleSerializer(articles, many=True)
    return Response(serialiers.data)

import pandas as pd
import sqlite3
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

con = sqlite3.connect("db.sqlite3", check_same_thread=False)
le = LabelEncoder()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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

    deposit_test['gender'] = le.fit_transform(deposit_train['gender'].values)[deposit_train[deposit_train['gender'].values == deposit_test['gender'].values].index[0]]
    deposit_test['job'] = le.fit_transform(deposit_train['job'].values)[deposit_train[deposit_train['job'].values == deposit_test['job'].values].index[0]]
    deposit_train['gender'] = le.fit_transform(deposit_train['gender'].values)
    deposit_train['job'] = le.fit_transform(deposit_train['job'].values)
    saving_test['gender'] = le.fit_transform(saving_train['gender'].values)[saving_train[saving_train['gender'].values == saving_test['gender'].values].index[0]]
    saving_test['job'] = le.fit_transform(saving_train['job'].values)[saving_train[saving_train['job'].values == saving_test['job'].values].index[0]]
    saving_train['gender'] = le.fit_transform(saving_train['gender'].values)
    saving_train['job'] = le.fit_transform(saving_train['job'].values)

    deposit_knn = KNeighborsClassifier(n_neighbors=3)
    deposit_knn.fit(deposit_train, deposit_target)
    deposit_pred = deposit_knn.predict_proba(deposit_test)
    saving_knn = KNeighborsClassifier(n_neighbors=3)
    saving_knn.fit(saving_train, saving_target)
    saving_pred = saving_knn.predict_proba(saving_test)

    deposit_res = pd.DataFrame(deposit_pred[0], columns=['pred_proba']).sort_values(by='pred_proba', ascending=False).head(3)
    deposit_idx = list(deposit_res.index)
    saving_res = pd.DataFrame(saving_pred[0], columns=['pred_proba']).sort_values(by='pred_proba', ascending=False).head(3)
    saving_idx = list(saving_res.index)

    deposits_recommend = Deposit.objects.filter(pk__in=deposit_idx)
    deposits_serializers = DepositSerializer(deposits_recommend, many=True)
    savings_recommend = Saving.objects.filter(pk__in=saving_idx)
    savings_serializers = SavingSerializer(savings_recommend, many=True)

    return Response({'deposit': deposits_serializers.data, 'saving': savings_serializers.data})
    
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def update(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerialzer(user)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    elif request.method == 'PUT':
        serializer = UserSerialzer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)