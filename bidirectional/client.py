import grpc
import bd_pb2
import bd_pb2_grpc



def generate_message():
    
    messages =[
        bd_pb2.ChatMessage(user="Client", message="Hello server"),
        bd_pb2.ChatMessage(user="Client", message="How are you server"),
        bd_pb2.ChatMessage(user="Client", message="Good Bye")
    ]
    
    for message in messages:
        yield message
        
def run():
    with grpc.insecure_channel('localhost:98765') as channel:
        stub = bd_pb2_grpc.ChatServiceStub(channel)
        responses= stub.chat(generate_message())
        for respones in responses:
            print(f"Received message from {respones.user}: {respones.message}")
            
            
            
if __name__ == "__main__":
    run()