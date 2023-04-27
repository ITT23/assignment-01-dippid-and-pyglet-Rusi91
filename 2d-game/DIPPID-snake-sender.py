import socket
import time

IP = '192.168.2.105'
PORT = 5700

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

counter = 0

while True:
    message = '{"heartbeat" : ' + str(counter) + '}'
    print(message)
    sock.sendto(message.encode(), (IP, PORT))

    counter += 1
    time.sleep(1)