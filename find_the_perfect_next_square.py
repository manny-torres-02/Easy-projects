import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    
    # Check if sq is a perfect square
    # If it is, find the next perfect square
    # If it isn't, return -1
    
    root =math.sqrt(sq)

    if int(root + 0.5) ** 2 == sq:
        print(root)
    else:
        return -1
    

    next = root + 1
    print(next*next)
    return next*next

    


find_next_square(121)