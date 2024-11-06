#while#

num = int(input("Enter a number: "))

total = 0
i = 1

while i <= num:
    total += i
    i += 1

print(f"The sum of numbers from 1 to {num} is: {total}")

#for#

num = int(input("Enter a number: "))

total = 0

for i in range(1, num + 1):
    total += i

print(f"The sum of numbers from 1 to {num} is: {total}")