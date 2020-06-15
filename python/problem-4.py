def largest_palindrome():
    palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            number = str(i * j)
            if len(number) == 6:
                if number[:3] == number[:2:-1]:
                    if int(number) > palindrome:
                        palindrome = int(number)
            else:
                if number[:2] == number[:2:-1]:
                    if int(number) > palindrome:
                        palindrome = int(number)
    return palindrome

print(largest_palindrome())
