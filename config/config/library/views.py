from rest_framework import viewsets
from .models import Book,Author
from .serializers import AuthorSerializer,BookSerializer

class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer