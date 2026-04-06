Network Compliance Port Auditor (Learning Project)

This is a basic Python project I developed as part of my learning journey into IT Compliance and Network Security. The goal of this project was to practice applying theoretical networking concepts (like TCP/IP and Port management) into a functional script.
The script acts as a simple auditor that scans a list of IP addresses to check if any "forbidden" ports are open, which would constitute a security violation in a hardened corporate environment.
 Learning Goals
I created this project to better understand:
TCP Handshaking: How a socket connection is established between a client and a server.
Network Security: Which ports (like 21, 23, and 3389) represent high risks and why they should be closed.
Python Automation: How to use loops and dictionaries to automate a repetitive manual auditing task.
Error Handling: Implementing timeouts to ensure the script handles unreachable hosts efficiently.
🛠️ How it Works
Target List: The script iterates through a list of provided IP addresses.
Port Blacklist: It checks each IP against a dictionary of "Forbidden Ports" (e.g., FTP, Telnet, RDP).
Connection Attempt: Using Python's socket library, the script attempts a TCP connection to the port.
Audit Result:
If the connection is successful, it flags a VIOLATION.
If no forbidden ports are open, it marks the target as COMPLIANT.
