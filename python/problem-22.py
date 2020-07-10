# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

# Importing helper module
import string

# Open file
reader = open("files/p022_names.txt", "r")

# Save all the names in unique string to make easier the cleaning
names = str(*reader.readlines())

# Splitting the names by comma
names = names.split(",")

# Creating an interator that removes the quotation marks
iterator = map(lambda x: x.strip("\""), names)
names = [name for name in iterator]


# Initializing a dictionary with every letter
hash_names = {char: [] for char in string.ascii_uppercase}

# Hashing and sorting every name by the initial letter
for name in names:
    hash_key = name[0]
    hash_names[hash_key].append(name)

for hash_key in hash_names.keys():
    hash_names[hash_key].sort()

# Initializing a score dict and asssigning every letter a value by alphabet
letter_scores = {string.ascii_uppercase[i]: i + 1 for i in range(26)}

# Helper function to get name score
def get_name_score(name):
    score = 0
    for letter in name:
        score += letter_scores[letter]
    return score

# Initializing an empty dict for storing each letter score
scores = []

# Initializing counter to keep track of the name position
count = 1

# Getting each name score and append it to the scores list
for hash_key in hash_names.keys():
    key_score = 0
    for name in hash_names[hash_key]:
        name_score = get_name_score(name)
        name_score *= count
        key_score += name_score
        count += 1

    scores.append(key_score)

# Getting the accumulate score 
print(sum(scores)) # Answer: 871198282


reader.close()
