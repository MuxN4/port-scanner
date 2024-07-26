import socket
from utils import parse_arguments, scan_port_range

def main():
    try:
        args = parse_arguments()
        host = args.host
        start_port = args.start_port
        end_port = args.end_port

        if start_port > end_port:
            raise ValueError("Start port must be less than or equal to end port")

        # Scan the range of ports and print their status
        for port in range(start_port, end_port + 1):
            result = scan_port_range(host, port)
            status = 'Open' if result else 'Closed'
            print(f"Port {port}: {status}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

