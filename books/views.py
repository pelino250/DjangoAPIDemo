# from django.http import HttpResponse, JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from books.models import Book
from books.serializers import BookSerializer


# Books endpoint Class-based view
class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)


