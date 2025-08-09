from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.utils import timezone
from .models import BorrowModel
from books.models import BookModel
from user.models import UserProfile
from .serializers import BorrowSerializer

class BorrowBookView(generics.CreateAPIView):
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        book_id = request.data.get('book_id')
        user = request.user

        if not book_id:
            return Response({"error": "book_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                book = BookModel.objects.select_for_update().get(pk=book_id)
                
                active_borrows_count = BorrowModel.objects.filter(user=user, return_date__isnull=True).count()
                if active_borrows_count >= 3:
                    return Response({"error": "Borrowing limit exceeded (max 3 books)."}, status=status.HTTP_400_BAD_REQUEST)
                
                if book.available_copies <= 0:
                    return Response({"error": "This book is not currently available."}, status=status.HTTP_400_BAD_REQUEST)

                borrow = BorrowModel.objects.create(user=user, book=book)
                book.available_copies -= 1
                book.save()
            
            serializer = self.get_serializer(borrow)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except BookModel.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

class BorrowListView(generics.ListAPIView):
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BorrowModel.objects.filter(user=self.request.user, return_date__isnull=True)

class ReturnBookView(generics.UpdateAPIView):
    queryset = BorrowModel.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        borrow_id = request.data.get('borrow_id')
        user = request.user

        if not borrow_id:
            return Response({"error": "borrow_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                borrow = BorrowModel.objects.select_for_update().get(pk=borrow_id, user=user, return_date__isnull=True)
                
                borrow.return_date = timezone.now().date()
                borrow.save()

                book = borrow.book
                book.available_copies += 1
                book.save()

                daysLate = (borrow.return_date - borrow.due_date).days
                if daysLate > 0:
                    profile = UserProfile.objects.get(user=user)
                    profile.penalty_points += daysLate
                    profile.save()
            
            serializer = self.get_serializer(borrow)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except BorrowModel.DoesNotExist:
            return Response({"error": "Active borrow record not found or already returned."}, status=status.HTTP_404_NOT_FOUND)

class UserPenaltyView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = None 
    permission_classes = [IsAuthenticated]
    lookup_field = 'user_id' 

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        return UserProfile.objects.get(user__id=user_id)
        
    def retrieve(self, request, *args, **kwargs):
        user_profile = self.get_object()
        return Response({"penalty_points": user_profile.penalty_points})