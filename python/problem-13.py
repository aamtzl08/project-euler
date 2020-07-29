import math

# Open file
reader = open("files/p013_number.txt", "r")

acc = 0
while (True):
    chunk = reader.readline()
    if (len(chunk) == 0):
        break
    acc += int(chunk) 

print(str(acc)[:10])
reader.close()


