
from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = "__all__"
        
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=AuthorModel.objects.all(), write_only=True, source='author')
    category_id = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all(), write_only=True, source='category')
    
    class Meta:
        model = BookModel
        fields = ['id', 'title', 'description', 'author', 'author_id', 'category', 'category_id', 'total_copies', 'available_copies']
        
    