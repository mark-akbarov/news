from rest_framework import generics
from .serializers import ArticleSerializer
from articles import models


class ArticleListAPIView(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer

# Create your views here.
