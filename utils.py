import argparse
import socket

def parse_arguments():
    parser = argparse.ArgumentParser(description="A simple port scanner to check open ports on a host.")
    parser.add_argument("host", help="The target host to scan (e.g., example.com or 192.168.1.1).")
    parser.add_argument("start_port", type=int, help="The starting port number for the scan.")
    parser.add_argument("end_port", type=int, help="The ending port number for the scan.")
    return parser.parse_args()

def scan_port_range(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        try:
            sock.connect((host, port))
        except (socket.timeout, socket.error):
            return False
        return True
