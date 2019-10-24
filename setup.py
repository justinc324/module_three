import socket
import platform
from psonic import *
from threading import Thread, Condition, Event

PIANO_MODE = '0'
SAMPLER_MODE = '1'
BASS_MODE = '2'

ZERO = '-1'

change_mode_cmds = {'0', '1', '2'}

# data we'll pass on to the program
# info/setup for connecting to the ESP32
# UDP_IP = "192.168.1.2"
# UDP_PORT = 57222
# sock = socket.socket(socket.AF_INET, # Internet
#                           socket.SOCK_DGRAM)  # UDP
# sock.bind((UDP_IP, UDP_PORT))
#
# class readUDP(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.running = True
#         self.data = None;
#         self.addr = None;
#         self.start()
#
#     def run(self):
#         while self.running:
#             self.data, self.addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#
#     def stop(self):
#         self.running = False
# # grab the correct serial port for Mac or Linux
# if platform.system() == 'Darwin':
#     ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)
# elif platform.system() == 'Linux':
#     ser = serial.Serial('/dev/ttyUSB0', 9600)
