from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from .services import GameService, MoveService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("grpc_server", server)
    app_registry.register(GameService)
    app_registry.register(MoveService)