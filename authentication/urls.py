from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('user/registration/', RegistrationAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path(
        'user/refresh-token/',
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh"),
    path(
        'user/logout/',
        jwt_views.TokenBlacklistView.as_view(),
        name="token_blacklist"),
]
