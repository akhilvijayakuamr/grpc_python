from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc


# class Greeter(helloworld_pb2_grpc.greeterServicer):
#     def SayHello(self, request, context):
#         return helloworld_pb2.HelloReply(response=f"Hello {request.name}")
    
# def server():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     helloworld_pb2_grpc.add_greeterServicer_to_server(Greeter(), server)
#     server.add_insecure_port('[::]:5051')
#     server.start()
#     server.wait_for_termination()

# if __name__ == '__main__':
#     server()


# class hai(helloworld_pb2_grpc.greeterServicer):
#     def SayHello(self, request, context):
#         return helloworld_pb2.HelloReply(response = f"Hello {request.name} I am server")
    
# def server():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     helloworld_pb2_grpc.add_greeterServicer_to_server(hai(), server)
#     server.add_insecure_port('[::]:78901')
#     server.start()
#     server.wait_for_termination()

    
# if __name__ == '__main__':
#     server()



# class Hai(helloworld_pb2_grpc.greeterServicer):
#     def SayHello(self, request, context):
#         return helloworld_pb2.HelloReply(response = f"Hello {request.name} I am server")
    
    
# def server():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     helloworld_pb2_grpc.add_greeterServicer_to_server(Hai(), server)
#     server.add_insecure_port('[::]:76549')
#     server.start()
#     server.wait_for_termination()
    
    
# if __name__ == '__main__':
#     server()




class re(helloworld_pb2_grpc.greeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(response = f"Am the server {request.name}")
    
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_greeterServicer_to_server(re(), server)
    server.add_insecure_port('[::]:12345')
    server.start()
    server.wait_for_termination()
    
    
if __name__ == '__main__':
    server()
    