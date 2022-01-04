from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'body',
            'date',
            'author',
        )
        model = Article