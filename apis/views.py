from django.db.models import query
from rest_framework import generics, serializers

from articles import models 
from .serializers import AricleSerializer


class ListArticle(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializers_class = AricleSerializer


class DetailArticle(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializers_class = AricleSerializer