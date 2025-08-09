from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BorrowBookView,ReturnBookView,BorrowListView,UserPenaltyView
from django.urls import path,include





urlpatterns = [
    path("borrow/",BorrowBookView.as_view()),
    path("borrow_list/", BorrowListView.as_view()),
    path("return/", ReturnBookView.as_view()),
    path('users/<int:id>/penalties/', UserPenaltyView.as_view(), name='user-penalties'),
]