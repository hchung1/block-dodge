from client import main_client
import os
import socket, platform
from uuid import getnode as get_mac
import getpass
def big_mac():
    mac = get_mac()
    h = iter(hex(mac)[2:-1].zfill(12))
    mac = ":".join(i + next(h) for i in h)
    username = getpass.getuser()
    return mac, username
def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    address = (s.getsockname()[0])
    s.close()
    platforms = platform.system()
    return address, platforms
#keep track of the score
def scorer(score):
    location = os.getcwd()
    locations = location.split('/')
    path = ("/{}/{}/.jokes".format(locations[1],locations[2]))
    os.chdir(path)
    if os.path.isfile("scores.txt") == False:
        f = open("scores.txt", "w+")
        f.write("0+0+0")
    if os.path.isfile("scores.txt") == True:
        f = open("scores.txt", "r")
        score_list = (f.read()).split("+")
        score_list[-1] = score_list[-1].strip()
        f.close()
    score_list.append(score)
    score_list = sorted(score_list, key=int, reverse=True)
    del score_list[-1]
    result = '+'.join(str(x) for x in score_list)
    f = open("scores.txt", "w+")
    f.write(result)
    f.close()
    os.chdir(location)
#grab data into print format for high score list
def reader():
    location = os.getcwd()
    locations = location.split('/')
    path = ("/{}/{}/.jokes".format(locations[1],locations[2]))
    os.chdir(path)
    try:
        f = open("scores.txt", "r")
        score_list = (f.read()).split("+")
        score_list[-1] = score_list[-1].strip()
        f.close()
        score_list = ', '.join(str(x) for x in score_list)
    except:
        score_list = "0, 0, 0"
    os.chdir(location)
    return score_list
#
def checked (inputs, data):
    f = open(inputs, "r")
    text = f.read()
    f.close()
    texts = text.split("+")
    x = 0
    for i in texts:
        if i == str(data):
            x = 1
    if x == 0:
        f = open(inputs, "w+")
        a = str(text + "+" + data)
        f.write(a.replace('\n', ''))
        print a
        f.close()
#Check if directory with information exist
def check_files():
    mac, name = big_mac()
    ip, platform = get_my_ip()
    location = os.getcwd()
    locations = location.split('/')
    t_path = ("/{}/{}".format(locations[1],locations[2]))
    path = ("/{}/{}/.jokes".format(locations[1],locations[2]))
    try:
        os.chdir(path)
    except:
        os.chdir(t_path)
        os.mkdir('.jokes')
        os.chdir('.jokes')
    if os.path.isfile("mac.txt") == False:
        f = open("mac.txt", "w+")
        f.write(mac + "+" + ip + "+" + platform + "+" + name)
        f.close()
    os.chdir(location)
    main_client()
