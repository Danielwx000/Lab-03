from collections import defaultdict

def ip_parse(line):
   
    if " from " in line:
        parts = line.split()
        try:
            anchor = parts.index("from")
            ip = parts[anchor+1]
            return ip.strip()
            
        except (ValueError, IndexError):
            return None
        
    return None

instances = defaultdict(int)           # Create a dictionary to keep track of IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            ip = ip_parse(line)
            if ip:
                instances[ip] += 1
print(instances)