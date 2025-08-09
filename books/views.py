from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import AuthorModel, BookModel
from .serializers import AuthorSerializer , BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class AuthorViewset(viewsets.ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
    
class BookViewset(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
