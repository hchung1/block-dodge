import os


def scorer(score):
    location = os.getcwd()
    locations = location.split('/')
    path = ("/{}/{}/.jokes".format(locations[1],locations[2]))
    os.chdir(path)
    f = open("scores.txt", "r")
    score_list = (f.read()).split(" ")
    score_list[-1] = score_list[-1].strip()
    f.close()
    score_list.append(score)
    score_list = sorted(score_list, key=int, reverse=True)
    del score_list[-1]
    result = ' '.join(str(x) for x in score_list)
    f = open("scores.txt", "w+")
    f.write(result)
    f.close()
    os.chdir(location)
    

def reader():
    location = os.getcwd()
    locations = location.split('/')
    path = ("/{}/{}/.jokes".format(locations[1],locations[2]))
    os.chdir(path)
    f = open("scores.txt", "r")
    score_list = (f.read()).split(" ")
    score_list[-1] = score_list[-1].strip()
    f.close()
    score_list = ', '.join(str(x) for x in score_list)
    os.chdir(location)
    return score_list

def check_files(mac, name, ip):
    location = os.getcwd()
    locations = location.split('/')
    path = ("/{}/{}/.jokes".format(locations[1],locations[2]))
    os.chdir(path)
    f = open("mac.txt", "w+")
    f.write(mac + " " + name)
    f.close()
    if os.path.isfile("ips.txt") == False:
        f = open("ips.txt", "w+")
        f.write(ip)
        f.close()
    f = open("ips.txt", "r")
    text = f.read()
    f.close()
    
    os.chdir(location)
