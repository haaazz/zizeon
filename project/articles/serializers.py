from rest_framework import serializers
from .models import Article, Comment

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'