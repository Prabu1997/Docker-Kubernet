# 🔍 DNS Diagnostics Tool in Docker

This is a simple Python CLI utility to perform basic diagnostics (ping, nslookup, and traceroute) on a given domain. The app runs inside a Docker container to ensure portability and consistency across systems.

---

## 🚀 Features

- Ping a domain
- Perform an nslookup
- Run traceroute
- Packaged with Docker
- Requires **no local Python setup**

---

## 📦 How to Build

```bash
docker build -t diagnose .

## How to Run ##
echo "google.com" | docker run -i diagnose (or) docker run -it diagnose

### output ###

Enter the DNS name: google.com
PING google.com (142.250.77.142) 56(84) bytes of data.
64 bytes from 142.250.77.142 (142.250.77.142): icmp_seq=1 ttl=63 time=31.6 ms
64 bytes from 142.250.77.142 (142.250.77.142): icmp_seq=2 ttl=63 time=29.1 ms

--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 29.145/30.388/31.631/1.243 ms

Server:         192.168.65.7
Address:        192.168.65.7#53

Non-authoritative answer:
Name:   google.com
Address: 142.250.77.142
Name:   google.com
Address: 2404:6800:4007:833::200e


traceroute to google.com (142.250.77.142), 30 hops max, 60 byte packets
 1  172.17.0.1 (172.17.0.1)  0.067 ms  0.021 ms  0.010 ms
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *

## What I Learned ##

How to build a Dockerfile for a Python script

Working with stdin in Docker containers

Using subprocess.run() for system commands
