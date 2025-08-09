from django.shortcuts import render
from rest_framework import  viewsets
from .models import CategoryModel
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class CategoryViewset(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()