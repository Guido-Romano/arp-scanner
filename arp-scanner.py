#!/usr/bin/env python3

import scapy.all as scapy
import socket

def get_local_network():
    # Get the local IP address
    local_ip = socket.gethostbyname(socket.gethostname())
    # Extract the first three octets to build the Class C network range
    network_prefix = ".".join(local_ip.split(".")[:3]) + ".0/24"
    return network_prefix

def scan(ip_range):
    # Perform an ARP scan on the given IP range
    scapy.arping(ip_range)

def main():
    # Automatically determine the Class C network based on the local IP
    target = get_local_network()
    print(f"Scanning the network: {target}")
    scan(target)

if __name__ == "__main__":
    main()