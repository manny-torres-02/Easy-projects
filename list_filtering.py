def filter_list(l):
    # 'return a new list with the strings filtered out'
    
    placeholder =[]
    for item in l:
        if isinstance(item, int):
            placeholder.append(item)
            print(placeholder)
    return placeholder
            
    # print(placeholder)
    # return placeholder
            
filter_list([1, 2, 'a', 'b'])