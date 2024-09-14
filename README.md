# Port Scanner
scans a range of ports on a specified host to identify open and closed ports, supports multi-threading for faster scanning. 

## Features

- Scan a range of ports on a specified host
- Multi-threaded for faster scanning
- User-friendly output format
- Adjustable number of threads


## Installation

1. Clone the repository or download the files.
2. Navigate to the project directory.

```bash
cd port_scanner
```

## Usage
To run the port scanner, use the following command:

```bash
python port_scanner.py <host> <start_port> <end_port> [--threads <num_threads>]
```
## Arguments

 - host: The host to scan (e.g., 127.0.0.1).
 - start_port: The starting port number (e.g., 20).
 - end_port: The ending port number (e.g., 80).
 - --threads: (Optional) The number of threads to use (default is 10).

## Example
```bash
python port_scanner.py 127.0.0.1 20 80 --threads 50
```
This command scans ports 20 to 80 on the host 127.0.0.1 using 50 threads.

## Notes
 - Ensure you have the necessary permissions to scan ports on the target host.
