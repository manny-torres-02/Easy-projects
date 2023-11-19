def minimum(arr):
    #your code here...
    small =arr[0]
    for i in arr:
        if i < small:
            small = i 
            
    print(small)
    return small 

def maximum(arr):
    #...and here
    large=arr[0]
    for i in arr:
        if i > large:
            large = i 
            
    print(large)
    return large 

minimum([-52, 56, 30, 29, -54, 0, -110])

maximum([-52, 56, 30, 29, -54, 0, -110])