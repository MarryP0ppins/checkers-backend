from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

import spectacular.urls
from app.views import *

router = routers.DefaultRouter()
router.register(r'user-info', UserInfoViewSet, basename='user-info')

urlpatterns = [
    path('', include(spectacular.urls)),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('authentication.urls', namespace='authentication')),
]
