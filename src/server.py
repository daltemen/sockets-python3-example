import socket

from client import HOST_URL, PORT
from cipher import decipher_word


def server():
    socket_obj = socket.socket()
    socket_obj.bind((HOST_URL, PORT))

    socket_obj.listen(1)
    connection, address = socket_obj.accept()
    print(f'Connection from: {address}')
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        print(f'from connected user: {data}')
        data = str(data)
        decrypted_word = decipher_word(data)
        print (f'sending: {decrypted_word}')
        connection.send(decrypted_word.encode())
    connection.close()


if __name__ == '__main__':
    server()