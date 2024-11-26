#whiledef sum_up_to_number():
    while True:
        try:
            user_input = input("Enter a positive integer (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            number = int(user_input)
            if number < 1:
                print("Please enter a positive integer greater than 0.")
                continue

            total_sum = 0
            current = 1

            while current <= number:
                total_sum += current
                current += 1

            print(f"The sum of all numbers from 1 to {number} is: {total_sum}")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Run the function
if __name__ == "__main__":
    sum_up_to_number() summation code following directions from Readme
