# Network Scanner using Scapy

This Python script performs network scanning using ARP requests to discover devices on the local network.

## Installation

Before running the script, make sure you have Scapy installed. You can install it using pip:

```bash
pip install scapy
```

## Alternative way is to download my repo and activate venv from Scripts

NetworkScanner >> Scripts >> Activate 
->>run command from Projetcs folder

##you can build your own python venv  [visit this website](https://docs.python.org/3/library/venv.html)


#To use the network scanner, run the script NetworkScanner.py with the following command-line options:
 -->give this commad to target network

```bash
python NetworkScanner.py -t <target>
```

#example
```bash
python NetworkScanner.py -t 192.168.1.0/24
```

##ScreenShot of Output:

![Scanning output](https://github.com/MuHIUDDIn98/Py_Networking.git/Py_Networking/NetworkScanner/screeShot/network scanner output.PNG)

