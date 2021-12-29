from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from . import (Serializers, models)
from rest_framework import viewsets, filters


class UserAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class = Serializers.UserSerializers
    queryset = models.User.objects.all()
    pagination_class = None

    def get_queryset(self):
        return [self.request.user]

    def list(self, request, *args, **kwargs):
        return Response(super().list(request, *args, **kwargs).data[0]) if len(super().list(request, *args, **kwargs).data) == 1 else super().list(request, *args, **kwargs)


class ProjectAPI(viewsets.ModelViewSet):
    serializer_class = Serializers.ProjectSerializers
    queryset = models.Project.objects.all()
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        self.queryset = models.Project.objects.filter(user=self.request.user)
        return self.queryset


class ProjectNewsAPI(viewsets.ModelViewSet):
    serializer_class = Serializers.ProjectNewsSerializers
    queryset = models.ProjectNews.objects.all()
    pagination_class = None

    def get_queryset(self):
        self.queryset = models.ProjectNews.objects.filter(project__user=self.request.user)
        return self.queryset





class NewsAPI(viewsets.ModelViewSet):
    serializer_class = Serializers.NewsSerializers
    queryset = models.News.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = [field.name for field in models.News._meta.fields]
    search_fields = [field.name for field in models.News._meta.fields]









