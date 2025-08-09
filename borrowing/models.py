from django.db import models
from user.models import User
from books.models import BookModel
from datetime import timedelta
from django.utils import timezone


class BorrowModel(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    borrow_date =  models.DateField(default=timezone.now)
    due_date = models.DateField()
    return_date = models.DateField(null= True , blank= True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.due_date = self.borrow_date + timedelta(days=14)
        super().save(*args, **kwargs)
        
    def __str__(self):
     return f"{self.book.title} (Borrow ID: {self.id})"
        
        
    
    
