def abbrev_name(name):
    test = name.split() 
    print(test)
    first = test[0]
    second = test[1]
    print(first)
    print(second)
     
    new = first[0].upper()+'.'+second[0].upper()
    print(new)
    return new
    