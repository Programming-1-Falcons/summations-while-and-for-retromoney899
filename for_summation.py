def sum_up_to_number():
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

            # Using a for loop to calculate the sum
            for i in range(1, number + 1):
                total_sum += i

            print(f"The sum of all numbers from 1 to {number} is: {total_sum}")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Run the function
if __name__ == "__main__":
    sum_up_to_number()#for Summation code here
