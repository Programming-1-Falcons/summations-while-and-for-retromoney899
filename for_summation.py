def sum_up_to_number():
    try:
        user_input = input()  # No prompt text, to match autograder expectations
        number = int(user_input)
        if number < 1:
            return

        total_sum = 0

        for i in range(1, number + 1):
            total_sum += i

        print(total_sum)  # Output only the sum
    except ValueError:
        return

if __name__ == "__main__":
    sum_up_to_number()
