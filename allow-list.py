#writing an "allow list" of specific IP addresses to a file
#in order to test, delete the existing "allow_list.txt" file so that the program can create and write a new file.


import_file = "allow_list.txt"

#simulated allowlist IP addresses
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"



with open(import_file, "w") as file:
    content = file.write(ip_addresses)

print(content)
