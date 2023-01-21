import socket
import json
import requests

def port_scan(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def whois(domain):
    url = f"https://api.whois.is/whois/{domain}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

domain = input("Enter an IP or URL: ")
ports = range(1, 65535)
open_ports = port_scan(domain, ports)
print(f"Open ports for {domain}: {open_ports}")
whois_data = whois(domain)
print(f"WHOIS data for {domain}: {whois_data}")
