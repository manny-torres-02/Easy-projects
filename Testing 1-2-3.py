def number(lines):
    #your code here
    arr = [] 
    counter = 0 
    for line in lines:
        
        # print(line)
        counter += 1
        arr.append((f"{counter}: {line}"))
        # arr.append = str(counter) + ": " + line
        # return array /
    # print(lines)
    print(arr)
    return arr
    
number(["a", "b", "c"])