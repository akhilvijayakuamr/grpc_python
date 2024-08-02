from concurrent import futures
import grpc
import cs_pb2_grpc
import cs_pb2

class res(cs_pb2_grpc.csgreeterServicer):
    def sayHai(self, request_iterator, context):
        result = ""
        for i in request_iterator:
            result += i.name
        return cs_pb2.HelloReply(response=f"The answer is {result}")
    
    
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cs_pb2_grpc.add_csgreeterServicer_to_server(res(), server)
    server.add_insecure_port('[::]:5678')
    server.start()
    server.wait_for_termination()
    
    
if __name__ == '__main__':
    server()
        