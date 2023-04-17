import socket
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def chatbot_server():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # get local machine name
    host = socket.gethostname()                           
    
    port = 9999
    
    # bind to the port
    serversocket.bind((host, port))                                  
    
    # queue up to 5 requests
    serversocket.listen(5)                                           
    
    print("Chatbot server is ready to receive client requests...")
    
    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()      
        
        print("got a connection from %s" % str(addr))
        
        message = clientsocket.recv(1024).decode()
        print("Received message: %s" % message)
        
        response = handle_message(message)
        
        clientsocket.send(response.encode())
        
        clientsocket.close()

def handle_message(message):
    emailId = "text-davinci-002"
    response = openai.Completion.create(
        engine=emailId,
        prompt=f"{message}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    return response

if __name__ == "__main__":
    chatbot_server()
