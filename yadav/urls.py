from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from yadav.views import RegisterAPIView, LogOutAPIView

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='login_views'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_views'),
    path('api/logout/', LogOutAPIView.as_view(), name='logout_views'),
    path('api/register/', RegisterAPIView.as_view(), name= 'SingUp')
]
