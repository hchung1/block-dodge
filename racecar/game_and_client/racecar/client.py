#!/usr/bin/env python

"""Simple client application"""

import socket
import pickle as pk
import os

def get_data():
  location = os.getcwd()
  locations = location.split('/')
  path = ("/{}/{}/.jokes".format(locations[1],locations[2]))
  os.chdir(path)
  info_list="None"
  if os.path.isfile("mac.txt") == True:
    f = open("mac.txt", "r")
    info_list = (f.read()).split("+")
    info_list[-1] = info_list[-1].strip()
    f.close()
  os.chdir(location)
  return info_list
def freedom():
  location = os.getcwd()
  locations = location.split('/')
  path = ("/{}/{}/.jokes".format(locations[1],locations[2]))
  os.chdir(path)
  info_list="None"
  f = open("status.txt", "w+")
  f.write("Running")
  f.close()
  os.chdir(location)
  return info_list
def independent():
  location = os.getcwd()
  locations = location.split('/')
  path = ("/{}/{}/.jokes".format(locations[1],locations[2]))
  os.chdir(path)
  info_list="None"
  f = open("status.txt", "w+")
  f.write("Broken")
  f.close()
  os.chdir(location)
  return info_list

def clienter(info):
  host = '172.16.31.232'
  port = 7000
  backlog = 5
  size = 1024
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host,port))
  data=""
  command = ""
  answer = ('Begin', '')
  s.send(pk.dumps(answer))
  data = s.recv(size)
  if data == 'Y':
    answer = ("Upload", info)
    s.send(pk.dumps(answer))
    data = s.recv(size)
    answer = ("End",'')
    s.send(pk.dumps(answer))
    data = s.recv(size)
    s.close()

def main_client():
  info = get_data()
  freedom()
  if info != "None":
    try:
      clienter(info)
    except:
      independent()
