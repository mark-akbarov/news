from rest_framework import serializers
from articles import models

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'body',
            'date',
            'author',
        )
        model = models.Article