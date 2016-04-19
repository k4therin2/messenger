#!/usr/bin/env python

import socket
import string
#Possible COMMANDS for INBOX are "requestAmount" and "getMessage - number"
def readCommand(data):
        devID = ''
        command = ''
        x = 0
        while data[x] != '|':      #This gets us the DevID in the case of an in$
            devID = devID + data[x]
            x = x + 1
        x = x + 1
        while data[x] != '|':
            command = command + data[x]
            x = x + 1
	if command == 'requestAmount':
            #here we handle getting the number of messages in inbox
            return '5' #return the number found
        elif command == 'getMessage':
            arg1 = ''
            x = x + 1
            while data[x] != '|':
                arg1 = arg1 + data[x]
                x = x + 1
            return 'This is a test message' #return the message string here
        elif command == 'sendMessage':
            target = ''
            message = ''
            x = x + 1 #move pointer to beginning of next arg
            while data[x] != '|':
                target = target + data[x]
                x = x + 1
            x = x + 1 #move pointer to next arg
            while data[x] != '|':
                message = message + data[x]
                x = x + 1
            #post message to targets inbox and notify target
            #host2 = '172.19.14.201' #GET TARGETS IP INTO THIS FIELD SOMEHOW
            #port2 = 81
            #size2 = 2048
            #s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #s2.connect((host,port))
            #s2.send('Activate the thing')
            #s2.close
            return 'success'  #return success
        else:
            return 'unable to process command'
host = ''
port = 80
backlog = 5
size = 4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    print data
    if data:
	response = readCommand(data)	
        client.send(response)
    client.close() 
