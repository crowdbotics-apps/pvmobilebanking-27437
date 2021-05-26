from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskerProfileViewSet,
    CustomerProfileViewSet,
    NotificationViewSet,
    InviteCodeViewSet,
)

router = DefaultRouter()
router.register("notification", NotificationViewSet)
router.register("customerprofile", CustomerProfileViewSet)
router.register("invitecode", InviteCodeViewSet)
router.register("taskerprofile", TaskerProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
