## Ben Alvaro, started 31/05/2024
## To not be used on any network that you don't have permission to run
## Disclaimer: I do not take responsibility for any malicious or ignorant 
## Use of this software, especially that of which is illegal. 

import socket
import threading
from queue import Queue

target = "153.107.45.15" ##MHS IP Address
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Uh Oh! Port {} is open!".format(port))
            open_ports.append(port)
        else:
            print("Port {} is closed!".format(port))
def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)

run_scanner(100, 1)
