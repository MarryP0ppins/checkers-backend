# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from grpc_server.grpc import grpc_server_pb2 as grpc__server_dot_grpc_dot_grpc__server__pb2


class GameControllerStub(object):
    """import "google/protobuf/struct.proto";

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/grpc_server.GameController/Create',
                request_serializer=grpc__server_dot_grpc_dot_grpc__server__pb2.CreateGameRequest.SerializeToString,
                response_deserializer=grpc__server_dot_grpc_dot_grpc__server__pb2.GameResponse.FromString,
                )
        self.PartialUpdate = channel.unary_unary(
                '/grpc_server.GameController/PartialUpdate',
                request_serializer=grpc__server_dot_grpc_dot_grpc__server__pb2.CreateGamePartialUpdateRequest.SerializeToString,
                response_deserializer=grpc__server_dot_grpc_dot_grpc__server__pb2.GameResponse.FromString,
                )


class GameControllerServicer(object):
    """import "google/protobuf/struct.proto";

    """

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PartialUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=grpc__server_dot_grpc_dot_grpc__server__pb2.CreateGameRequest.FromString,
                    response_serializer=grpc__server_dot_grpc_dot_grpc__server__pb2.GameResponse.SerializeToString,
            ),
            'PartialUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.PartialUpdate,
                    request_deserializer=grpc__server_dot_grpc_dot_grpc__server__pb2.CreateGamePartialUpdateRequest.FromString,
                    response_serializer=grpc__server_dot_grpc_dot_grpc__server__pb2.GameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_server.GameController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GameController(object):
    """import "google/protobuf/struct.proto";

    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_server.GameController/Create',
            grpc__server_dot_grpc_dot_grpc__server__pb2.CreateGameRequest.SerializeToString,
            grpc__server_dot_grpc_dot_grpc__server__pb2.GameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PartialUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_server.GameController/PartialUpdate',
            grpc__server_dot_grpc_dot_grpc__server__pb2.CreateGamePartialUpdateRequest.SerializeToString,
            grpc__server_dot_grpc_dot_grpc__server__pb2.GameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MoveControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/grpc_server.MoveController/Create',
                request_serializer=grpc__server_dot_grpc_dot_grpc__server__pb2.CreateMoveRequest.SerializeToString,
                response_deserializer=grpc__server_dot_grpc_dot_grpc__server__pb2.MoveResponse.FromString,
                )


class MoveControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MoveControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=grpc__server_dot_grpc_dot_grpc__server__pb2.CreateMoveRequest.FromString,
                    response_serializer=grpc__server_dot_grpc_dot_grpc__server__pb2.MoveResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_server.MoveController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MoveController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_server.MoveController/Create',
            grpc__server_dot_grpc_dot_grpc__server__pb2.CreateMoveRequest.SerializeToString,
            grpc__server_dot_grpc_dot_grpc__server__pb2.MoveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
