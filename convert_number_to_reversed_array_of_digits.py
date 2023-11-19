def digitize(n):
    
    arr =[]
    for i in str(n):
        arr.insert(0,int(i))
        
    print(arr)
    return


digitize(35231) # [1,3,2,5,3]