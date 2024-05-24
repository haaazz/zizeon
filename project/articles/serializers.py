from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
    class ArticleUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')
    user = ArticleUserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class CommentUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')
    user = CommentUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article',)