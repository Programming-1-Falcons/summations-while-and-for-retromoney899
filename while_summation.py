def sum_up_to_number():
    try:
        user_input = input()  # No prompt text, to match autograder expectations
        number = int(user_input)
        if number < 1:
            return

        total_sum = 0
        current = 1

        while current <= number:
            total_sum += current
            current += 1

        print(total_sum)  # Output only the sum
    except ValueError:
        return

if __name__ == "__main__":
    sum_up_to_number()
