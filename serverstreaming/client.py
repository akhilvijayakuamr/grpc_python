import grpc
import ss_pb2
import ss_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:98765') as channel:
        stub = ss_pb2_grpc.ssgreeterStub(channel)
        req_message = ss_pb2.HelloRequest(request="test request")
        respo = stub.sayOi(req_message)
        for r in respo:
            print(r.response)
            
            
if __name__ == '__main__':
    run()