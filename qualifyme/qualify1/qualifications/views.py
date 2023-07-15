from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Qualification
from .serializers import QualificationSerializer

class QualificationView(generics.ListCreateAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class QualificationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
