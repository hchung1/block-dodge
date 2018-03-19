from get_ip import get_my_ip
from get_mac import big_mac
from librarian import check_files
import os
mac, name = big_mac()
ip = get_my_ip()
check_files(mac, name, ip)
