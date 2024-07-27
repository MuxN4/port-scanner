from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import parse_arguments, scan_port_range, format_output

def main():
    try:
        args = parse_arguments()
        host = args.host
        start_port = args.start_port
        end_port = args.end_port
        num_threads = args.threads

        if start_port > end_port:
            raise ValueError("Start port must be less than or equal to end port")

        # List to store all open ports found
        open_ports = []

        #ThreadPoolExecutor for concurrent port scanning
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            #A dictionary to keep track of the port scanning tasks
            futures = {executor.submit(scan_port_range, host, port): port for port in range(start_port, end_port + 1)}
            for future in as_completed(futures):
                port = futures[future]
                # Checks if a port is open and adds to the list if it is
                if future.result():
                    open_ports.append(port)
                print(f"Port {port}: {'Open' if future.result() else 'Closed'}")

        print("\nScan Results:")
        print(format_output(open_ports))

    except ValueError as e:
        print(f"invalid port range: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
