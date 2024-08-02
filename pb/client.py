import grpc
import helloworld_pb2
import helloworld_pb2_grpc


# def run():
#     with grpc.insecure_channel('localhost:5051') as channel:
#         stub = helloworld_pb2_grpc.greeterStub(channel)
#         response = stub.SayHello(helloworld_pb2.HelloRequest(name="Akhil"))
#     print(f"The client received: {response.response}")
    


# if __name__ == '__main__':
#     run()


# def run():
#     with grpc.insecure_channel('localhost:78901') as channel:
#         stub = helloworld_pb2_grpc.greeterStub(channel)
#         response = stub.SayHello(helloworld_pb2.HelloRequest(name="Megha"))
#     print(f"Client recevied from serrver {response}")
    
    
# if __name__ == '__main__':
#     run()


# def client():
#     with grpc.insecure_channel('localhost:76549') as channel:
#         stub = helloworld_pb2_grpc.greeterStub(channel)
#         reply=stub.SayHello(helloworld_pb2.HelloRequest(name="Shivaraj"))
#     print(f"The message is came {reply}")
    
    
# if __name__ == '__main__':
#     client()



def client():
    with grpc.insecure_channel('localhost:12345') as channel:
        stub = helloworld_pb2_grpc.greeterStub(channel)
        reply=stub.SayHello(helloworld_pb2.HelloRequest(name="Sanup"))
    print(f"The notification is cammed {reply}")
    
    
    
if __name__ == '__main__':
    client()