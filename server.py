# Tarefa: Programação com sockets


import socket

HOST = ''
PORT = 8081 

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((HOST, PORT))

listen_socket.listen(1)

print ('Serving HTTP on port %s ...' % PORT)

while True:
    client_connection, client_address = listen_socket.accept()
   
    request = client_connection.recv(1024).decode()
  
    request = request
    request = request.split(" ")
    print(request)
    if(request[0] == 'GET'):
        file = request[1].split(" ")
        print(file[0][1:])
        if(file[0] == "/"):
            index = open('index.html')
            contend = index.read()
            http_response = """HTTP/1.1 200 OK\r\n\r\n""" + str(contend)
            index.close()
        else: 
            try:
                response = open(file[0][1:])
                contend = response.read()
                http_response = """HTTP/1.1 200 OK\r\n\r\n""" + str(contend)
                response.close()
            except:
                not_found = open("not_found.html")
                contend = not_found.read()
                http_response = """HTTP/1.1 404 Not Found\r\n\r\n""" + contend
                not_found.close()
    else:
        bad_request = open('bad_request.html')
        contend = bad_request.read()
        http_response = """HTTP/1.1 400 Bad Request\r\n\r\n""" + str(contend)
        bad_request.close()
    
    
 
    
    client_connection.send(http_response.encode('utf-8'))

    client_connection.close()

listen_socket.close()