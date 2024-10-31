import re

def check_ip_address(ip):
    ipv4_pattern = r'^((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    
    if re.match(ipv4_pattern, ip):
        segments = ip.split('.')
        if all(0 <= int(segment) <= 255 for segment in segments):
            return "IPv4"
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    else:
        return "Bukan IP Address"

def main():
    n = int(input("Masukkan jumlah baris input: "))
    
    results = []
    for _ in range(n):
        ip_input = input().strip()
        
        if len(ip_input) > 500:
            results.append("\nBukan IP Address")
        else:
            results.append(check_ip_address(ip_input))
    
    for result in results:
        print(result)

main()
