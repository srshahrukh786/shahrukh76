from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from qualifications.serializers import QualificationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(detail=True, methods=['get'])
    def qualifications(self, request, pk=None):
        user = self.get_object()
        qualifications = user.qualifications.all()
        serializer = QualificationSerializer(qualifications, many=True)
        return Response(serializer.data)


# Create your views here.
