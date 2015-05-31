import RPi.GPIO as GPIO
import time
import socket
import sys

PIN_BCK = 11
PIN_FWD = 15
PIN_LFT = 13
PIN_RGT = 12
pin_red=7
pin_green=18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_RGT,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_LFT,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_FWD,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_BCK,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_red,GPIO.OUT)
GPIO.setup(pin_green,GPIO.OUT)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#server_address = ('localhost', 10000)
server_address = ('192.168.1.113', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
GPIO.output(pin_green,GPIO.LOW)
GPIO.output(pin_red,GPIO.HIGH)

try:
    prev = 'SSSS'    
    while True:

	#print str(GPIO.input(11)) + ' ' + str(GPIO.input(13)) + ' ' + str(GPIO.input(15)) + ' ' + str(GPIO.input(12))
	if GPIO.input(PIN_RGT) == 0 and prev == 'SSSS':
 		GPIO.output(pin_red,GPIO.LOW)
                GPIO.output(pin_green,GPIO.HIGH)
		prev = 'RRRR'
		print 'right'	
    		message = 'RRRR'
    		sock.sendall(message)
    		while GPIO.input(PIN_RGT) == 0:
			pass
 		GPIO.output(pin_green,GPIO.LOW)
                GPIO.output(pin_red,GPIO.HIGH)
		sock.sendall('SSSS')
		prev = 'SSSS'
	if GPIO.input(PIN_FWD) == 0 and prev == 'SSSS':
 		GPIO.output(pin_red,GPIO.LOW)
                GPIO.output(pin_green,GPIO.HIGH)
		print 'forward'	
    		message = 'FFFF'
    		sock.sendall(message)
    		while GPIO.input(PIN_FWD) == 0:
			pass
 		GPIO.output(pin_green,GPIO.LOW)
                GPIO.output(pin_red,GPIO.HIGH)
		sock.sendall('SSSS')
		prev = 'SSSS'
	if GPIO.input(PIN_LFT) == 0 and prev == 'SSSS':
 		GPIO.output(pin_red,GPIO.LOW)
                GPIO.output(pin_green,GPIO.HIGH)
		print 'left'	
    		message = 'LLLL'
    		sock.sendall(message)
    		while GPIO.input(PIN_LFT) == 0:
			pass
 		GPIO.output(pin_green,GPIO.LOW)
                GPIO.output(pin_red,GPIO.HIGH)
		sock.sendall('SSSS')
		prev = 'SSSS'
	if GPIO.input(PIN_BCK) == 0 and prev == 'SSSS':
 		GPIO.output(pin_red,GPIO.LOW)
                GPIO.output(pin_green,GPIO.HIGH)
		print 'back'	
    		message = 'BBBB'
    		sock.sendall(message)
    		while GPIO.input(PIN_BCK) == 0:
			pass
 		GPIO.output(pin_green,GPIO.LOW)
                GPIO.output(pin_red,GPIO.HIGH)
		sock.sendall('SSSS')
		prev = 'SSSS'

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
    GPIO.output(pin_green,GPIO.LOW)
    GPIO.output(pin_red,GPIO.LOW)



