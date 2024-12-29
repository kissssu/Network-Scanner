# Network Scanner

A Python-based script that scans a network for live hosts, retrieves their MAC addresses, and identifies their vendors. This tool is helpful for network administrators and penetration testers to gain insights into devices in a network.

---

## Features
- Sends ARP requests to detect live hosts in the network.
- Displays the IP address, MAC address, and vendor information of detected hosts.
- User-friendly output in a tabular format using PrettyTable.

---

## Requirements
1. **Python 3.6+**
2. Install the required libraries:
   ```bash
   pip install scapy prettytable mac-vendor-lookup
    ```

## Usage

1. Run the Script:
```bash
python3 network_scanner.py --h 192.168.1.0/24
```
 
2. Example Output:
```
+-----------------+-------------------+------------------+
|       IP        |       MAC         |      VENDOR      |
+-----------------+-------------------+------------------+
| 192.168.1.1     | 00:1A:2B:3C:4D:5E| Cisco Systems     |
| 192.168.1.10    | 00:1E:AA:BB:CC:DD| Dell Inc.         |
+-----------------+-------------------+------------------+
```

## Arguments
- ```--h``` or ```--hosts```: Specify one or more hosts or a subnet to scan.
Example:
```bash
python3 network_scanner.py --h 192.168.1.0/24 192.168.1.10
```

## How It Works
- **ARP Request**: Sends ARP requests to the specified hosts/subnet.
- **Response Handling**: Identifies live hosts based on ARP replies.
- **MAC Address Lookup**: Resolves the MAC addresses to their corresponding vendors using the mac-vendor-lookup library.
- **Tabular Output**: Displays the results in a table format.

## Limitations
- Requires administrator privileges to send ARP packets.
- Only works on networks where ARP requests can be sent and responses can be received.

## Disclaimer
This tool is for **educational and authorized network auditing purposes only.** Unauthorized use is strictly prohibited.

## License
This project is licensed under the MIT License. See LICENSE for details.
