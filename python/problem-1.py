multiples = []

for number in range(1, 1000):
    if not number % 3 or not number % 5:
        multiples.append(number)

print(sum(multiples))
