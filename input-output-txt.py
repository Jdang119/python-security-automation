#program that imports opens, reads, and parses the file for readability 
#program then writes and appends a "missing" entry 
#text file contains simulated user logins with timestamp and IP addresses



#relative pathing for user testing on personal machines
import_file = 'logins-log.txt'

#simulated missing entry
missing_entry = "testuser,192.168.243.140,4:56:27,2022-05-09"

#importing log file and storing as string, passing in "a" for append
with open(import_file, "a") as file:
    content = file.write(missing_entry)


#importing, reading, and printing contents after appending entry to file
with open(import_file, "r") as file:
    content = file.read()
    print(content)




