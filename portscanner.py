import socket

port_names = {
    21 : "FTP",
    22 : "SSH",
    23 : "Telnet",
    25 : "SMTP",
    53 : "DNS",
    80 : "HTTP",
    135: "RPC",
    443: "HTTPS",
    445: "SMB",
    3306 :"MySQL",
    8080 : "HTTP-ALT"
}  


def scan_ports(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except:
        return False

#Testing the port scanner

host = "127.0.0.1"
print(f"Scanning {host} for open ports...")
for port in range (1, 1000):
    if scan_ports(host, port):
        port_name = port_names.get(port, "Unknown")
        print(f"Port {port} ({port_name}) is OPEN !")
print("Port scanning completed !")
