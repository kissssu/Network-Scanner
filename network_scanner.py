#!/usr/bin/python3

from scapy.all import *
from prettytable import PrettyTable
from mac_vendor_lookup import MacLookup
from argparse import ArgumentParser
import sys

class NetworkScanner:
    def __init__(self, hosts):
        self.alive = {}  # Initialize alive dictionary once
        for host in hosts:
            self.host = host
            self.create_packet()
            self.send_packet()
            self.get_alive()

    def create_packet(self):
        layer1 = Ether(dst="ff:ff:ff:ff:ff:ff")
        layer2 = ARP(pdst=self.host)
        packet = layer1 / layer2
        self.packet = packet

    def send_packet(self):
        answered, unasnwered = srp(self.packet,timeout=1,verbose=False)
        if answered:
            self.answered = answered
        else:
            print("No Host is up")
            sys.exit(1)

    def get_alive(self):
        for sent, recevied in self.answered:
            self.alive[recevied.psrc] = recevied.hwsrc

    def print_alive(self):
        table = PrettyTable(["IP","MAC","VENDOR"])
        for ip, mac in self.alive.items():
            try:
                table.add_row([ip,mac,MacLookup().lookup(mac)])
            except:
                table.add_row([ip,mac,"Unknown"])
        print(table)

def get_args():
    parser = ArgumentParser(description="Network Scanner")
    parser.add_argument("--h", dest="hosts", nargs="+", help="Hosts to scan")
    arg = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return arg.hosts

hosts = get_args()
NetworkScanner(hosts)