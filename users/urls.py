from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView
)

from .views import UserViewset, social_auth

router = DefaultRouter()

router.register('users', UserViewset)

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('auth/social/<str:backend>/', social_auth, name='social-auth'),
    path('', include(router.urls)),
]