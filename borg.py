import socket
import sys
import PicoBorgRev
import time
import math

PBR = PicoBorgRev.PicoBorgRev()
#PBR.i2cAddress = 0x44                  # Uncomment and change the value if you have changed the board address
PBR.Init()
if not PBR.foundChip:
    boards = PicoBorgRev.ScanForPicoBorgReverse()
    if len(boards) == 0:
        print 'No PicoBorg Reverse found, check you are attached :)'
    else:
        print 'No PicoBorg Reverse at address %02X, but we did find boards:' % (PBR.i2cAddress)
        for board in boards:
            print '    %02X (%d)' % (board, board)
        print 'PBR.i2cAddress = 0x%02X' % (boards[0])
    sys.exit()
#PBR.SetEpoIgnore(True)                 # Uncomment to disable EPO latch, needed if you do not have a switch / jumper
PBR.SetCommsFailsafe(False)             # Disable the communications failsafe
PBR.ResetEpo()

msgs = ['RRRR', 'LLLL', 'FFFF', 'BBBB','SSSS']
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('192.168.1.113', 10000)
#server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

def moveFwd():
    PBR.SetMotor1(1)
    PBR.SetMotor2(-1)

def moveBck():
    PBR.SetMotor1(-1)
    PBR.SetMotor2(1)

def moveLft():
    PBR.SetMotor1(-1)
    PBR.SetMotor2(-1)

def moveRgt():
    PBR.SetMotor1(1)
    PBR.SetMotor2(1)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        while True:
            data = connection.recv(4)
            print >>sys.stderr, 'received "%s"' % data
            print 'length ' + str(len(data))
            if data in msgs:
                print >>sys.stderr, 'sending ack back to the client'
                connection.sendall('ACK')
		if data == 'RRRR':
			print 'moving right'
			moveRgt()
		if data == 'SSSS':
			PBR.MotorsOff()
			print 'stopping'
		if data == 'LLLL':
			print 'moving left'
			moveLft()
		if data == 'FFFF':
			moveFwd()
			print 'FFFFF'
		if data == 'BBBB':
			print 'BACK'
			moveBck()
            else:
                print >>sys.stderr, 'unknown  data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
