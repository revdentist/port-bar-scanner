import socket

target = "scanme.nmap.org"

print(f"Scanning {target}...\n")

for port in range(1, 1001):
    s = socket.socket()
    s.settimeout(0.1)
    try:
        s.connect((target, port))
        print(f"Port {port} is OPEN")
    except:
        pass
    s.close()
