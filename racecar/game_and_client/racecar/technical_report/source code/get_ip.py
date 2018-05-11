 #!/usr/bin/python
import socket

def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    address = (s.getsockname()[0])
    s.close()
    return address