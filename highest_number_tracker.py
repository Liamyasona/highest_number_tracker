# Program to ask user to input 5 numbers and will print the highest number

def highest_number(var1, var2, var3):
    highest = None

    # Ask user to input 5 numbers 
    for i in range(5):
        user_number = float(input(f"Enter number {i + 1}: "))

        # Find highest number
        if highest is None or user_number > highest:
            highest = user_number
    
    # Print the highest number
    print(f"The highest number is: {highest}")
    
# Compose var1 to var 5
# If var 1 is greater than all variables
    # compare var 1 to var 2
    # if var 1 is greater than var 2
    # compare it to other variables
    # if highest var is found, print 