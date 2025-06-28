from ipwhois import IPWhois
import socket

def lookup(target):
    try:
        # Convert domain to IP if needed
        ip = socket.gethostbyname(target)
        print(f"[+] Resolved {target} to IP: {ip}")

        object = IPWhois(ip)
        result = object.lookup_rdap()

        print("\n[+] WHOIS Information:")
        print(f"  - ASN: {result.get('asn')}")
        print(f"  - CIDR: {result.get('network', {}).get('cidr')}")
        print(f"  - Org: {result.get('network', {}).get('name')}")
        print(f"  - Country: {result.get('network', {}).get('country')}")

    except Exception as e:
        print(f"[-] Error: {e}")


if __name__ == "__main__":
        target = input('Usage: python whois_lookup.py <domain_or_ip>')
        lookup(target)
        

