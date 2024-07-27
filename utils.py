import argparse
import socket

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple Port Scanner with Multi-threading")
    parser.add_argument("host", help="Host to scan") 
    parser.add_argument("start_port", type=int, help="Starting port number") 
    parser.add_argument("end_port", type=int, help="Ending port number")  
    parser.add_argument("--threads", type=int, default=10, help="Number of threads to use")  
    return parser.parse_args()

def scan_port_range(host, port):
    # Creating a new socket for each port to be checked
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1) 
        try:
            sock.connect((host, port)) 
        except (socket.timeout, socket.error):
            return False  # If it times out or errors, the port is closed
        return True  # successful connection, the port is open

def format_output(open_ports):
    if open_ports:
        return f"Open Ports: {', '.join(map(str, open_ports))}" 
    else:
        return "No open ports found." 
