from concurrent import futures
import grpc
import bd_pb2
import bd_pb2_grpc
import time


class ChatService(bd_pb2_grpc.ChatServiceServicer):
    def chat(self, request_iterator, context):
        for chat in request_iterator:
            print(f"Received from {chat.user}: {chat.message}")
            yield bd_pb2.ChatMessage(user="server", message=f"echo:{chat.message}")
            
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bd_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:98765')
    server.start()
    try:
        while(True):
            time.sleep(8765)
    except KeyboardInterrupt:
        server.stop(0)
    
if __name__ == '__main__':
    server()
    
    
    