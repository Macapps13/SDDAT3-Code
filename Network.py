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
