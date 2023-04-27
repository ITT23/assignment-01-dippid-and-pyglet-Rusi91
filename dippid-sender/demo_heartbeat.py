from DIPPID import SensorUDP
from time import sleep

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

def handle_hearbeat(data):
    print(data)

def handle_accelerometer(data):
    print(data)
    
def handle_button_one(data):
    if int(data) == 1:
        print('button was released')
    else:
        print('button was pressed')

sensor.register_callback('heartbeat', handle_hearbeat)
sensor.register_callback('accelerometer', handle_accelerometer)
sensor.register_callback('button_1', handle_button_one)

# show all capabilites of the sensor and check if specific accelerometer axes are readable/accessible 
while(True):
    # all capabilities of the sensor
    print('capabilities: ', sensor.get_capabilities())

    if(sensor.has_capability('accelerometer')):

        # print only one accelerometer axis x
        print('accelerometer X: ', sensor.get_value('accelerometer')['x'])

    sleep(5)
