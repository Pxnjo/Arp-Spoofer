import subprocess
import re
from scapy.all import ARP, Ether, srp
import ipaddress

result = subprocess.run(
    ["ipconfig", "-all"], 
    capture_output=True, text=True, 
    encoding="cp1252", errors="replace"
)

output = result.stdout
lines = output.split('\n')

capturing = False
eth_info = []

for line in lines:
    # Inizia a catturare quando troviamo la scheda Ethernet specifica
    if "Scheda Ethernet Ethernet:" in line:
        capturing = True
        eth_info.append(line.strip())
    # Continua a catturare IPv4 e Subnet mask
    elif capturing and ("IPv4" in line or "Subnet" in line):
        eth_info.append(line.strip())
    # Fine di cattura

class NetworkInterface:
    def __init__(self, item):
        self. item = item
    
    def attribute(self):
        pattern = r":\s*(\d+\.\d+\.\d+\.\d+)"
        match = re.search(pattern, self.item)
        if match:
            attribute = match.group(1)
            return attribute


for item in eth_info:
    if "IPv4" in item:
        ipv4 = NetworkInterface(item)
        print(f"IPv4: {ipv4.attribute()}")
    elif "Subnet" in item:
        subnet = NetworkInterface(item)
        print(f"Subnet: {subnet.attribute()}")

pattern = r"(\d+\.\d+\.\d+)"
match = re.search(pattern, ipv4.attribute())
if match:
    network_ipv4 = match.group(1)
network = ipaddress.IPv4Network(f'{network_ipv4}.0/24', strict=False)

broadcast_ip = network.broadcast_address
print(f"Broadcast IP: {broadcast_ip}")

ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # L'indirizzo MAC di broadcast
arp = ARP(pdst=str(broadcast_ip))  # Impostiamo l'indirizzo di broadcast come destinazione

packet = ether/arp

# Invia il pacchetto ARP e raccogli le risposte
result = srp(packet, timeout=3, verbose=False)[0]

# Estrai gli IP e i MAC degli apparati che hanno risposto
devices = []
for sent, received in result:
    devices.append({"ip": received.psrc, "mac": received.hwsrc})

# Mostra gli IP e MAC dei dispositivi che hanno risposto
if result:
    for sent, received in result:
        print(f"Risposta ARP ricevuta da {received.psrc} con MAC {received.hwsrc}")
else:
    print("Nessuna risposta ARP ricevuta.")