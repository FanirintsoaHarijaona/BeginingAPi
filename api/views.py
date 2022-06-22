from django.shortcuts import render
from rest_framework import generics
from book.models import Book
from .serializer import BookSerializer
# Create your views here.

class BookAPIView(generics.ListAPIView):
    queryset            =   Book.objects.all()
    serializer_class    =   BookSerializer


