# ARP Spoofer - Network Tool

## 🛠️ **Description**

This is a small tool created out of the necessity to contact an ONT (Optical Network Terminal) which, according to the instruction manual, should have had the IP `192.168.1.1`. However, since it was impossible to reach it at that IP, I thought that maybe the IP was different. But who would want to manually try all possibilities? Using an existing tool would have been too easy, so I decided to create my own. Don't worry, it's not malicious! 😄

## 💡 **How it Works**

This tool performs an ARP scan in the local network to find the correct IP address of the ONT. It does this by broadcasting ARP requests and listening for replies, effectively mapping the network.

### Features:
- **IP Detection**: Identifies devices on the network.
- **ARP Broadcast**: Sends ARP requests to the broadcast IP.
- **Safe and Easy to Use**: It's designed for legitimate use only. 

## 📌 **Important Note**
This tool is intended for legitimate use, such as finding devices in your own network. It is not meant for malicious activities like network attacks or unauthorized access.

## ⚙️ **Installation**

1. Install Python (3.x+).
2. Install necessary dependencies:

```bash
pip install scapy
```
# ⚠️ Disclaimer
### _This tool is meant solely for educational purposes or personal network maintenance. Using it on a network without permission is illegal and unethical._
