import socket
import platform
from psonic import *
from threading import Thread, Condition, Event

RIGHT = b'RIGHT\r\n'
LEFT = b'LEFT\r\n'
UP = b'UP\r\n'
DOWN = b'DOWN\r\n'

joystick_cmds = {RIGHT, LEFT, UP, DOWN}

BUTTON_PRESSED = b'-1\r\n'

DRUM_MODE = b'0\r\n'
PIANO_MODE = b'1\r\n'
BELLS_MODE = b'2\r\n'
SAMPLER_MODE = b'3\r\n'
BASS_MODE = b'4\r\n'

change_mode_cmds = {DRUM_MODE, PIANO_MODE, BELLS_MODE, SAMPLER_MODE, BASS_MODE}

# data we'll pass on to the program
data = None
addr = None
# info/setup for connecting to the ESP32
UDP_IP = "192.168.1.2"
UDP_PORT = 57222
sock = socket.socket(socket.AF_INET, # Internet
                          socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

class readUDP(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes

# # grab the correct serial port for Mac or Linux
# if platform.system() == 'Darwin':
#     ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)
# elif platform.system() == 'Linux':
#     ser = serial.Serial('/dev/ttyUSB0', 9600)
