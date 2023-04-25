import socket
import time
import numpy as np

IP = '127.0.0.1'
PORT = 5700

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

counter = 0

# In order to implement a plausible behavior for the simulated sensors 
# sine of random degrees were used for each axis.
def get_sine_of_random_degree():
    # get random degree between 1 and 360
    random_degree = np.random.randint(1,360)
    # in order to calculate the sine first the radiant must be calculated
    radiant_of_degree = np.radians(random_degree)
    return np.sin(radiant_of_degree)

while True:
    # create messages
    message = '{"heartbeat" : ' + str(counter) + '}'
    
    message_accelerometer = '{"accelerometer" : {"x" : ' + str(get_sine_of_random_degree()) + \
        ', "y" : '  + str(get_sine_of_random_degree()) + \
            ', "z" : '  + str(get_sine_of_random_degree()) + '}' + '}'
    
    # send messages
    sock.sendto(message_accelerometer.encode(), (IP, PORT))
    sock.sendto(message.encode(), (IP, PORT))
    
    # check messages
    print(message_accelerometer)
    print(message)

    counter += 1
    time.sleep(1)
    
    