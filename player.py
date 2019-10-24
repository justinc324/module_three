from setup import *
from instruments import *

i = 0

drum = Drum()
piano = Piano()
bells = BellSynth()
bass = Bass()
sampler = Sampler()
modes = ["DRUMS_MODE", "PIANO_MODE", "BELLS_MODE", "SAMPLER_MODE", "BASS_MODE"]

curr_mode = modes[1]

samples = {'-2', '-3', '-4',
			'-5', '-6'}

# start listening to server
UDP_IP = "192.168.1.2"
UDP_PORT = 57222

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	command, addr = sock.recvfrom(1024)

	command = command.decode('utf-8')

	if command == "-1":
		print("SHIt")

	if command:

		if command in change_mode_cmds:

			print("shit")

			if command == PIANO_MODE:
				curr_mode = modes[1]

			elif command == SAMPLER_MODE:
				curr_mode = modes[3]

			elif command == BASS_MODE:
				curr_mode = modes[4]

			print(curr_mode)

		elif command in samples:
			if command == b'-2\r\n':
				i = 0

			elif command == b'-3\r\n':
				i = 1

			elif command == b'-4\r\n':
				i = 2

			elif command == b'-5\r\n':
				i = 3

			elif command == b'-6\r\n':
				i = 4

			if curr_mode is "PIANO_MODE":

				piano.play(i)
				print("piano start")

			elif curr_mode is "SAMPLER_MODE":

				sampler.play(i)
				print("sampler play")

			elif curr_mode is "BASS_MODE":
				bass.play(i)
				print("bass play")

		elif command == ZERO:

			if curr_mode is "PIANO_MODE":

				piano.stop_loop()
				piano.is_looping = False
				print("piano stop")

			elif curr_mode is "SAMPLER_MODE":

				sampler.stop_loop()
				sampler.is_looping = False
				print("sampler stop")

			elif curr_mode is "BASS_MODE":
				bass.stop_loop()
				bass.is_looping = False
				print("bass stop")
