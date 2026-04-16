# Phynet-Inspired Network Scanner

## Overview
This project is a Python-based network scanner designed to identify active devices on a local subnet. It scans a range of IP addresses, determines which hosts are reachable, and analyzes basic network structure.

## Features
- Scans a subnet for active IP addresses
- Identifies reachable devices using ICMP (ping)
- Converts discovered IPs into their network address
- Cross-platform support (Windows/Linux & macOS)

## How It Works
The script loops through a defined IP range and sends a ping request to each address. If a response is received, the IP is stored.

Each reachable IP is then processed:
- Split into octets (192.168.1.80 → ['192','168','1','80'])
- Remove the host portion
- Rebuild into a network address (192.168.1.0)

This helped reinforce real-world subnetting concepts and network structure.

## Example Output

## Future Improvements
- Add MAC address detection (ARP)
- Display response time (latency)
- Export results to file (CSV/JSON)
- Build UI using C# (.NET)

## Tech Stack
- C#
- Python
- OS / Platform module
- Basic networking (ICMP, subnetting)

## Purpose
Built to strengthen networking fundamentals through hands-on scripting while working in a data center environment.
