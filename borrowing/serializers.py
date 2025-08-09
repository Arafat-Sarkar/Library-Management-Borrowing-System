from rest_framework import serializers
from .models import BorrowModel
from books.models import BookModel
from books.serializers import BookSerializer

# class BorrowSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BorrowModel
#         fields = "__all__"

class BorrowSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=BookModel.objects.all(),
        write_only=True,
        source='book'
    )
   
    class Meta:
        model = BorrowModel
        fields = ('id', 'user', 'book', 'book_id', 'borrow_date', 'due_date', 'return_date')
        read_only_fields = ('borrow_date', 'due_date', 'return_date')

    