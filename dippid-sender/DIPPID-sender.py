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

# generate randomly the number 0 or 1
# in demo_heartbeat.py this numbers get interpreted as "0 = button 1 was pressed" and "1 = button 1 was released"
def get_random_button_one_press_event():
    random_number = np.random.randint(1,100)
    if random_number % 2 != 0 :
        return 0
    else:
        return 1

while True:
    # create messages
    message = '{"heartbeat" : ' + str(counter) + '}'
    
    message_accelerometer = '{"accelerometer" : {"x" : ' + str(get_sine_of_random_degree()) + \
        ', "y" : '  + str(get_sine_of_random_degree()) + \
            ', "z" : '  + str(get_sine_of_random_degree()) + '}' + '}'
            
    message_button_1 = '{"button_1" : ' + str(get_random_button_one_press_event()) + '}'
    
    # send messages
    sock.sendto(message.encode(), (IP, PORT))
    sock.sendto(message_accelerometer.encode(), (IP, PORT))
    sock.sendto(message_button_1.encode(), (IP, PORT))
    
    # check messages
    print(message_accelerometer)
    print(message)
    print(message_button_1)

    counter += 1
    # slower clock for testing purposes
    time.sleep(1)
    
    # For the current use of the acceloremeter, a faster clock would make more sense
    # time.sleep(0.1)
    
    