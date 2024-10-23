# arp-spoofing-python

This script allows you to sniff internet traffic between your network gateway and a machine connected to you local network by making an arp spoofing attack.

## Requirements

- Linux operating system (tested on Debian 8)
- (Python)
- [scapy](https://scapy.net/)

## Usage

### Installing scapy

Install scapy by typing the commands:
```bash
wget scapy.net
unzip scapy-latest.zip  # might be "unzip index.html"
cd scapy-2.*
sudo python setup.py install
```

or via `pip`

```bash
pip install scapy
```

### Launching

Launch the script using

```bash
sudo python arp-spoofing-python.py
```