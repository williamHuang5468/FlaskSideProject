# Tcp Chat server

import socket, select

#Function to broadcast chat messages to all connected clients
def broadcast_data (send_message_client, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if isServerOrSendMessageSocket(send_message_client):
            continue

        try :
            socket.send(message)
        except :
            # broken socket connection may be, chat client pressed ctrl+c for example
            socket.close()
            CONNECTION_LIST.remove(socket)

def isServerOrSendMessageSocket(send_message_client):
    return socket != server_socket and socket != send_message_client

if __name__ == "__main__":
    HOST="0.0.0.0"
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Init server socket
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(10)

        CONNECTION_LIST.append(server_socket)
        print("Chat server started on port ", str(PORT))

        while 1:
            # Get the list sockets which are ready to be read through select
            read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST,[],[])

            for sock in read_sockets:
                #New connection
                if sock is server_socket:
                    # Handle the case in which there is a new connection recieved through server_socket
                    connection, address = server_socket.accept()
                    CONNECTION_LIST.append(connection)
                    print("Client (%s, %s) connected") % address
                    broadcast_data(connection, "[%s:%s] entered room\n" % address)
                #Some incoming message from a client
                else:
                    # Data recieved from client, process it
                    try:
                        #In Windows, sometimes when a TCP program closes abruptly,
                        # a "Connection reset by peer" exception will be thrown
                        data = sock.recv(RECV_BUFFER)
                        if data:
                            broadcast_data(sock, "\r < {0} > {1}".format(str(sock.getpeername()), data))
                    except:
                        broadcast_data(sock, "Client (%s, %s) is offline" % address)
                        print("Client (%s, %s) is offline") % address
                        sock.close()
                        CONNECTION_LIST.remove(sock)
                        continue
