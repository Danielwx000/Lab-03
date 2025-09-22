# lab2-2_starter.py
import re 
ips = []
counter = 0
LOGFILE = "sample_auth_small.log"  # change filename if needed

def ip_parser(line):
   
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            ip = parts[anchor+1]          # the port value will be next token, anchor+1
            return ip.strip()             # strip any trailing punctuation
            
        except (ValueError, IndexError):
            return None

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


## This is the main block that will run first. 
## It will call any functions from above that we might need.

