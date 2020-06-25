# WARNING: You need to have the sequence in a .txt called 'sequence' for this code to work 

sequence = open('sequence.txt', 'r')
max_mult = 1
while True:
    mult = 1
    chunk =  sequence.read(13)
    pointer = sequence.tell()
    for number in chunk:
        if number == 0:
            break
        mult *= int(number)
    if mult > max_mult:
        max_mult = mult
    if pointer == 999:
        break
    else:
        sequence.seek(pointer - 12)
    


print(max_mult)
