from rest_framework import generics
from article.models import Article
from article.serializers import ArticleDetailSerializer, ArticleListSerializer
from rest_framework.permissions import IsAdminUser


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAdminUser]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
