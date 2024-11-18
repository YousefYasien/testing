from scapy.all import ARP, Ether, srp
import socket
import argparse

def scan_network(network_ip):
    """Scans a network for devices using ARP requests.

    Args:
        network_ip (str): The base IP of the network to scan (e.g., 192.168.1.1).

    Returns:
        list: A list of dictionaries, each containing device information (IP, MAC, Hostname).
    """
    # Define IP range to scan, e.g., '192.168.1.0/24'
    ip_range = f"{network_ip}.0/24"

    # Create ARP request
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Send packet and receive responses
    arp_responses = srp(arp_request_broadcast, timeout=2, verbose=0)

    # Store devices with IP, MAC, and device name
    devices = []
    for sent, received in arp_responses:
        ip = received.psrc
        mac = received.hwsrc
        try:
            # Try to get the hostname for each IP
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"  # If no hostname is found
        devices.append({'IP': ip, 'MAC': mac, 'Hostname': hostname})

    return devices

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Scan a network for devices.')
parser.add_argument('network_ip', type=str, help='The base IP of the network to scan (e.g., 192.168.1.1)')

args = parser.parse_args()
network_ip = args.network_ip  # Get the network IP from command line argument

# Run the scan and print results
devices = scan_network(network_ip)

print("Devices on the network:")
for device in devices:
    print(f"IP: {device['IP']}, MAC: {device['MAC']}, Hostname: {device['Hostname']}")