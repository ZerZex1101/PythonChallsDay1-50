import socket

def get_domain_name(ip_address):
    try:
        # Use the socket.gethostbyaddr() to get the domain name
        domain_name, _, _ = socket.gethostbyaddr(ip_address)
        return domain_name
    except socket.herror:
        return "No domain associated with this IP address."

# Example usage
ip = "8.8.8.8"
print(f"Domain name for IP {ip}: {get_domain_name(ip)}")
