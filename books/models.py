from django.db import models
from categorys.models import CategoryModel


class AuthorModel(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    def __str__(self):
         return(self.name) 
            
    
class BookModel(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    author = models.ForeignKey(AuthorModel, on_delete = models.CASCADE)
    category = models.ForeignKey(CategoryModel , on_delete=models.CASCADE)
    total_copies= models.IntegerField()
    available_copies = models.IntegerField()
    
    def __str__(self):
         return(self.title) 
