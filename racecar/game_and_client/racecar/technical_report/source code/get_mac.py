 #!/usr/bin/python
from uuid import getnode as get_mac
import getpass
def big_mac():
    mac = get_mac()
    h = iter(hex(mac)[2:-1].zfill(12))
    mac = ":".join(i + next(h) for i in h)
    username = getpass.getuser()
    return mac, username
