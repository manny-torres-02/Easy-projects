def square_digits(num):
    squared =""
    doubled = 0
    for i in str(num):
        print(int(i))
        doubled = int(i) * int(i)
        squared += str(doubled)
    print(squared)
    
    return str(squared)
        
        
square_digits(9119)