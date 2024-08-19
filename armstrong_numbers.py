def is_armstrong_number(number):
    # Create a placeholder to store the sum of the digits
    placeholder = 0 

    # Check if the number is a number or a string 
    if (type(number) != int):
        print("Invalid input. Please enter a number")
        raise ValueError("Invalid input. Please enter a number")
    else :
        print("The input is a number")
    
#   find the length of the number
    test_length = len(str(number))
    print(test_length)
    
#    Cycle through the digits within the number 
#    in order to cycle through each digit, convert the number to a string, as you can iterate through each digit in a string and not a number 
    for x in str(number):
        x = int(x)

        to_the_power = x**test_length
        placeholder = placeholder + to_the_power
        print(placeholder)
        
    if placeholder == number:
        print("The number is an Armstrong number")
    else:
        print("The number is not an Armstrong number")
        
    print(placeholder)
    return number==placeholder
        
is_armstrong_number(0)