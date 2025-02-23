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

## Upcoming Updates

This section outlines planned enhancements and features for future versions of the Network Scanner. Contributions and suggestions are welcome!

* **Asynchronous Scanning:** Implement asynchronous scanning using `asyncio` or threading to significantly improve scanning speed, especially for larger networks.
* **IP Range Input Flexibility:** Allow users to specify IP ranges in more flexible formats (e.g., CIDR notation, comma-separated lists, ranges with hyphens).
* **Output to File:** Enable users to save scan results to a file (CSV, JSON, or text) for later analysis and reporting.
* **Progress Bar:** Add a progress bar to provide visual feedback during scanning, especially helpful for large subnets.
* **Improved Error Handling:** Enhance error handling with `try...except` blocks to catch potential network issues or invalid input and provide more informative error messages.

We are actively working on these updates and will release them as they become available. Please stay tuned!

## Disclaimer
This tool is for **educational and authorized network auditing purposes only.** Unauthorized use is strictly prohibited.

## License
This project is licensed under the MIT License. See LICENSE for details.
