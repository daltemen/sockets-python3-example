import socket

from config import HOST_URL, PORT
from cipher import cypher_word


def client():
    socket_obj = socket.socket()
    socket_obj.connect((HOST_URL, PORT))

    print('Welcome Unkown, if you want to quit please press q ')
    message = input(" -> ")
    encrypted_word = cypher_word(message)

    while message != 'q':
        socket_obj.send(encrypted_word.encode())
        data = socket_obj.recv(1024).decode()
        print(f'Received from server: {data}')
        message = input(" -> ")
        encrypted_word = cypher_word(message)
    socket_obj.close()


if __name__ == '__main__':
    client()