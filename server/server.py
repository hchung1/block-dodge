#!/usr/bin/env python

"""Simple server application"""

from query_database import finder
import socket
import pickle as pk

host = socket.gethostbyname( '0.0.0.0' )
port = 7000
backlog = 5
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) 
s.listen(backlog)
while 1:
    print ('Server ready, willing and able!')
    client, address = s.accept()
    data = pk.loads(client.recv(size))
    if data[0] == 'Begin':
        client.send('Y')
        while data[0] != "End":
            data = pk.loads(client.recv(size))
            if data[0] == "Upload":
                result=finder(data[1][0],data[1][1],data[1][2])
                client.send(result)
                print (result)
            if data[0] == "End":
                client.send("Closed")
                client.close()
