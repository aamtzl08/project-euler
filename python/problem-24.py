def permute(single, sequence):
    perms = []
    for element in sequence:
        chars = [char for char in element]
        for i in range(len(chars) + 1):
            tmp = chars[:]
            tmp.insert(i, single)
            perms.append("".join(tmp))
        
    return perms

def permutations(sequence):
    length = len(sequence)
    if length == 1:
        return [sequence]
    else:
        return sorted(permute(sequence[0], permutations(sequence[1:])))

print(permutations('0123456789')[1000000-1])
