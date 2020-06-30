# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

number = str(2 ** 1000)
number_sum = 0

for char in number:
	number_sum += int(char)
	
print(number_sum)
