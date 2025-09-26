from collections import defaultdict
import time

def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

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

start = time.time()
instances = defaultdict(int)           # Create a dictionary to keep track of IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            ip = ip_parse(line)
            if ip:
                instances[ip] += 1

final_list = top_n(instances)
for i in final_list:
    print(i[0], i[1])

end = time.time()
print("Elapsed:", end-start, "seconds")

