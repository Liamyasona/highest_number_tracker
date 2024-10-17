# Program to find the highest number among five user-inputted numbers

def highest_number():
    # Store the highest number with a variable
    highest = None

    # Ask user to input 5 numbers
    # loop if statements using range to get 5 numbers from user
    for i in range(5):
        input_number = float(input(f"Please enter any number {i + 1}: "))
        
        # Update the highest number among the numbers using if statements
        if highest is None or input_number > highest:
            highest = input_number

    # Print the highest number
    print(f"The highest number is: {highest}")

# Execute the main function
if __name__ == "__main__":
    highest_number()
