def sum_up_to_number():
    try:
        user_input = input("Enter a positive integer: ")
        number = int(user_input)
        if number < 1:
            print("Please enter a positive integer greater than 0.")
            return

        total_sum = 0

        for i in range(1, number + 1):
            total_sum += i

        print(total_sum)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    sum_up_to_number()
