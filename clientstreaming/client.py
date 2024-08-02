import grpc
import cs_pb2
import cs_pb2_grpc



def gen_req():
    for i in range(5):
        yield cs_pb2.HelloRequest(name = f"The numbers are {i} ")

def run():
    with grpc.insecure_channel('localhost:5678') as channel:
        stub = cs_pb2_grpc.csgreeterStub(channel)
        response = stub.sayHai(gen_req())
    print(f"The result is =  {response}")
    
    
if __name__ == '__main__':
    run()
        