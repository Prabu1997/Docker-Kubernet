import os
import subprocess


def diagonse(domain_name):
    try:
        command1 = ["ping", "-c 10", domain_name]
        command2 = ["nslookup", domain_name]
        command3 = ["traceroute", domain_name]
        ping = subprocess.run(command1, capture_output=True, text=True)
        print(ping.stdout)
        nslookup = subprocess.run(command2, capture_output=True, text=True)
        print(nslookup.stdout)
        tracert = subprocess.run(command3, capture_output=True, text=True)
        print(tracert.stdout)

    except Exception as error:
        print("Program Error: ", error)


def main():
    domain_name = input("Enter the DNS name: ")
    diagonse(domain_name)


if __name__ == "__main__":
    main()
