## Ben Alvaro, started 31/05/2024
## To not be used on any network that you don't have permission to run
## Disclaimer: I do not take responsibility for any malicious or ignorant 
## Use of this software, especially that of which is illegal. 

import socket
import threading
from queue import Queue
import datetime

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
            openPortMsg = "Uh Oh! Port {} is open!".format(port)
            print(openPortMsg)
            with open(filename, 'a') as logs:
                logs.write(openPortMsg + ("\n"))
            open_ports.append(port)
        else:
            closedPortMsg = "Port {} is closed!".format(port)
            print(closedPortMsg)
            with open(filename, 'a') as logs:
                logs.write(closedPortMsg + ("\n"))
def run_scanner(threads, mode):
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    global filename
    filename = f"network_{timestamp}.txt"

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    open_ports_message = "Open ports are:", open_ports
    print(open_ports_message)
    with open(filename, 'a') as logs:
        logs.write(str(open_ports_message))







