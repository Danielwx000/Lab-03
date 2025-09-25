# lab2-2_starter.py
import re 
ips = []
counter = 0
LOGFILE = "sample_auth_small.log"

def ip_parser(line):
   
    if " from " in line:
        parts = line.split()
        try:
            anchor = parts.index("from")
            ip = parts[anchor+1]
            return ip.strip()
            
        except (ValueError, IndexError):
            return None

with open('sample_auth_small.log', 'r') as f:
    for line in f:
        ip_pattern = r"\d+\.\d+\.\d+\.\d+"
        found_ips = re.findall(ip_pattern,line)
        for ip in found_ips:
            ips.append(ip)
            #counter += 1 
unique_ips = set(ips)
print("Uniquie Ip's ")
for ip in unique_ips:
    counter += 1
    print(ip)

print("The ammount of unique ip's is", counter)
