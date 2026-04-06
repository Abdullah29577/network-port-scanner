import socket  # The library used for network connections

# --- CONFIGURATION ---
# Dummy IP addresses representing different corporate assets
# 127.0.0.1 = Localhost (Your machine)
# 10.0.0.x = Typical internal corporate subnet
TARGET_IPS = [
    "127.0.0.1", 
    "10.0.0.15", 
    "10.0.0.22", 
    "10.0.0.101", 
    "192.168.1.1"
] 

# A "Blacklist" of ports that should NEVER be open in a secure environment
FORBIDDEN_PORTS = {
    21: "FTP (Unencrypted File Transfer)",
    23: "Telnet (Unencrypted Remote Access)",
    3389: "RDP (Remote Desktop - High Risk)",
    80: "HTTP (Unencrypted Web)",
    445: "SMB (Windows File Sharing - Ransomware Risk)"
}

def scan_port(ip, port):
    """Attempts to connect to a specific port on an IP address."""
    # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout so the script doesn't hang (1 second)
    s.settimeout(1)
    
    # .connect_ex returns 0 if the connection is successful (Port is OPEN)
    result = s.connect_ex((ip, port))
    s.close()
    
    return result == 0

def main():
    print("--- Enterprise IT Network Compliance Audit ---")
    print(f"Scanning {len(TARGET_IPS)} targets for non-compliant ports...\n")

    for ip in TARGET_IPS:
        print(f"Auditing Target: {ip}")
        violations_found = 0
        
        for port, description in FORBIDDEN_PORTS.items():
            if scan_port(ip, port):
                print(f"  [!] VIOLATION: Port {port} ({description}) is OPEN!")
                violations_found += 1
        
        if violations_found == 0:
            print("  [+] Status: Compliant. No forbidden ports detected.")
        
        print("-" * 50)

if __name__ == "__main__":
    main()