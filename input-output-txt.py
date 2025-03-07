#program that imports opens, reads, and parses the file for readability 
#program then writes and appends a "missing" entry 
#text file contains simulated user logins with timestamp and IP addresses



#relative pathing for user testing on personal machines
import_file = 'logins-log.txt'

#importing, reading, and printing contents
with open(import_file, "r") as file:
    content = file.read()
    print(content)


