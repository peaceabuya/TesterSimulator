#!/usr/bin/python

# Import modules
import sys
import socket
import time

# Create socket object
s = socket.socket()
print s

def get_command(command):
	print s
	# Send ENQ and check ACK
	s.send('\x05')
	#time.sleep(.1)
	rsp = s.recv(1)
	while rsp != '\x06':
		s.send('\x05')
		#time.sleep(.1)
		rsp = s.recv(1)

	# Send command
	s.send(command)
	#time.sleep(.1)
	# Wait for ENQ
	rsp = s.recv(1)
	while rsp != '\x05':
		print 'Waiting for ENQ'
		rsp = s.recv(1)

	s.send('\x06')
	time.sleep(.1)
	rsp = s.recv(1024)
	print rsp
	return 1

def main(unused):
	# Host IP Address and Port Number
	host_ip = '172.26.67.100'
	host_port = 10001

	print s
	# Establish connection
	s.connect((host_ip, host_port))
	
	for i in xrange(5):
		print i
		start = time.time()
		get_command('\x02CD\x03')
		print time.time() - start
		get_command('\x02DHT\x03')
	return 0
	
	# Close connection
	s.close()
	
	print s

if __name__ == '__main__':
    sys.exit(main(sys.argv))