from django.urls import path
from .views import QualificationAPIView

urlpatterns = [
    path('qualifications/', QualificationAPIView.as_view(), name='Qualifications-list'),
    path('qualifications/', QualificationAPIView.as_view(), name='Qualifications-detail'),
]
