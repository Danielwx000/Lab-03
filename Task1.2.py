# lab2-2_starter.py
import re 
ips = []
ipcounter = 0
linecon = 0
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
        
    return None


with open('sample_auth_small.log', 'r') as f:
    for line in f:
        linecon += 1
        ip_pattern = r"\d+\.\d+\.\d+\.\d+"
        found_ips = re.findall(ip_pattern,line)
        for ip in found_ips:
            ips.append(ip)


unique_ips = set(ips)
sortedIps = sorted(unique_ips)
#print("Uniquie Ip's ")
for ip in unique_ips:
    ipcounter += 1
    #print(ip)
    

print("Lines read:  ", linecon)
print("Unique Ips:  ", ipcounter)
print("First 10 Ips: ", sortedIps[:10])
