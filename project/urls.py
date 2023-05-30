from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from app.views import *
#from grpc_server.handlers import grpc_handlers as grpc__handlers

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'game', GameViewSet, basename='game')
router.register(r'move', MoveViewSet, basename='move')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('authentication.urls', namespace='authentication')),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "doc/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

# def grpc_handlers(server):
#     grpc__handlers(server)