import nmap

target_ip = input("Please enter the target IP Address to scan:\n")
target_port = input("Please enter target Port to scan: \n")

nm = nmap.PortScanner()

try:
    nm.scan(target_ip, target_port)

    if target_ip in nm.all_hosts():
        if "tcp" in nm[target_ip]:
            if int(target_port) in nm[target_ip]["tcp"]:
                state = nm[target_ip]["top"][int(target_port)]["state"]
                print(f"Port {target_port} is: {state}")
            else:
                print(f"Port {target_port} is closed or filtered on {target_ip}")
        else:
            print(f"No TCP results found for {target_ip}")
    else:
        print(f"Host {target_ip} not found in scan results")

except Exception as e:
    print(f"An error occurred: {e}")


# import nmap

# target_ip = input("Please enter target IP address to scan: ")
# target_port = input("Please enter target Port to scan: ")
# print("Searching...")

# res = nmap.PortScanner().scan(target_ip, target_port)

# print("\n")
# print("Port " + target_port + " is: " + res['scan'][target_ip]['tcp'][int(target_port)]['state'])