import sys
import socket
import threading
import time


Usage = "Python3 port_scanner.py TARGET START_PORT END _PORT"

print("-"*70)
print("Python3 Simple Port Scanner")
print("-"*70)

start_time = time.time()

if(len(sys.argv) != 4):
    print(Usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resoluation erroe")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target",target)

def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target,port))
    if(not conn):
        print("Port {} is open".format(port))
    s.close()

for port in range(start_port,end_port+1):
    thread = threading.Thread(target = scan_port,args = (port,))
    thread.start()

end_time = time.time()
print("Time Elapsed",end_time - start_time)