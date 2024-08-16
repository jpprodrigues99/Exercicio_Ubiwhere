from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoadSegmentViewSet

router = DefaultRouter()
router.register(r'roadsegments', RoadSegmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
