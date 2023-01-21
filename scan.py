# -*- coding: scan -*-

# -*- coding: UTF-8 -*-

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

def whois(ip):
    url = f"https://whois.p whois-api.com/whois/search?api_key={api_key}&domain={ip}"
    response = requests.get(url)
    whois_data = json.loads(response.text)
    return whois_data

ip = input("Enter an IP or URL: ")
ports = range(1, 65535)
open_ports = port_scan(ip, ports)
print(f"Open ports for {ip}: {open_ports}")
whois_data = whois(ip)
print(f"WHOIS data for {ip}: {whois_data}")
