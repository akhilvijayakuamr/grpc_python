from concurrent import futures
import grpc
import ss_pb2
import ss_pb2_grpc


class se(ss_pb2_grpc.ssgreeterServicer):
    def sayOi(self, request, context):
        for i in range(5):
            resp = ss_pb2.HelloReply(response=f"message {i} for {request.request}")
            yield resp
            
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ss_pb2_grpc.add_ssgreeterServicer_to_server(se(), server)
    server.add_insecure_port('[::]:98765')
    server.start()
    server.wait_for_termination()
    
    
if __name__ == '__main__':
    server()