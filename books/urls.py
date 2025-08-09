from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewset , BookViewset
from django.urls import path,include
from categorys.views import CategoryViewset

router = DefaultRouter()
router.register("authors",AuthorViewset)
router.register("books", BookViewset)
router.register("category", CategoryViewset)

urlpatterns = [
    path("",include(router.urls)),
]