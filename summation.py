# summation assignment

def while_summation(num):
    "Sums up numbers from 1 to num using a while loop."
    total_sum = 0
    i = 1
    while i <= num:
        total_sum += i
        i += 1
    return total_sum

def for_summation(num):
    "Sums up numbers from 1 to num using a for loop."
    total_sum = 0
    for i in range(1, num + 1):
        total_sum += i
    return total_sum

num = int(input("Enter a number: "))

method = input("Choose method (while/for): ").strip().lower()

if method == "while":
    result = while_summation(num)
    print(f"The sum of numbers from 1 to {num} using a while loop is: {result}")
elif method == "for":
    result = for_summation(num)
    print(f"The sum of numbers from 1 to {num} using a for loop is: {result}")
else:
    print("Invalid method chosen. Please enter 'while' or 'for'.")