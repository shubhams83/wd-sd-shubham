
from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import TrySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Try1


# Create your views here.
class TryList(generics.ListAPIView):
    queryset = Try1.objects.all()
    serializer_class = TrySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]