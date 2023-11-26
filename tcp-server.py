#!/bin/python3

import socket
import threading
import argparse

# Function for server. Setting up listener, backlog to 5
# then loop while it waits for a connection

def server(IP, PORT):
    TCPserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPserv.bind((IP, PORT))
    TCPserv.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    # while loop. Multiple variable assignments to socket and
    # tuple holding client address.
    # client_handler starts handle_client with client, variable 
    while True:
        client, address = TCPserv.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

# Main function which specifies parser for input args and
# passes reassigned args through vars calling server function. 
if __name__ == '__main__':
    # argparse arguments from user
    parser = argparse.ArgumentParser()
    parser.add_argument("IP", help="Specify server's IP address", type=str)
    parser.add_argument("Port", help="Specify server's Port", type=int)
    args = parser.parse_args()

    # Assign argparse input(from above) to variables, so we can pass them into functions
    server_IP = args.IP
    server_Port = args.Port

    # Run server
    server(server_IP, server_Port)
