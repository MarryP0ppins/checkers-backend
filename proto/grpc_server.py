import grpc
import backend_pb2
import backend_pb2_grpc
from concurrent import futures
import socket
import socketio


sio = socketio.Client()
sio.connect('http://localhost:8080')
print(sio.sid)


class send_gameServicer(backend_pb2_grpc.WsProtoServicer):
    def createGameEvent(self, request, context):

        print('create')

        sio.emit('createGameRequest', {'Status': request.status,
                                        'user_1': request.user_1,
                                        'user_2': request.user_2})

        return backend_pb2.GameResponce(message = 'created')
    

    def editGameEvent(self, request, context):

        print('edit')

        sio.emit('joinGame', {"post": {
                                    "status": request.post.status,
                                    "user_1": request.post.user_1,
                                    "user_2": request.post.user_2
                                },
                                "user_1_points": request.user_1_points,
                                "status": request.status,
                                "finish_at": request.finish_at,
                                "user_1_turn": request.user_1_turn
                              })

        return backend_pb2.GameResponce(message = 'edited')
    

    def createMoveEvent(self, request, context):

        print('create move')

        sio.emit('playerMakeMove', { "checker_id": request.checker_id,
                                "game": request.game,
                                "is_king": request.is_king,
                                "is_white": request.is_white,
                                "new_positions": list(request.new_positions),
                                "user": request.user
                             })

        return backend_pb2.GameResponce(message = 'created move')

    
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    backend_pb2_grpc.add_WsProtoServicer_to_server(send_gameServicer(), server=server)
    print('server started')
    server.add_insecure_port('[::]:7000')
    server.start()
    server.wait_for_termination()

main()