# Network Scanner using Scapy

This Python script performs network scanning using ARP requests to discover devices on the local network.

## Installation

Before running the script, make sure you have Scapy installed. You can install it using pip:

```bash
pip install scapy

#To use the network scanner, run the script network_scanner.py with the following command-line options:

python network_scanner.py -t <target>
example
python network_scanner.py -t 192.168.1.1/24
