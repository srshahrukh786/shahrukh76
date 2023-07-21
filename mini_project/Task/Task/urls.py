from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from user.views import UserViewSet
from qualifications.views import QualificationViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'qualifications', QualificationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

