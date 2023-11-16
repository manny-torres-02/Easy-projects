def is_isogram(string):
    # your code here
    # convert to lowercase since this does not matter
    string = string.lower()
    # for loop to iterte through each letter
    for i in string:
        # Use string.count() to count the number of times a letter appears in the string
        # if it appears more than once then return False
        if string.count(i) > 1:
            return False
    #  if it does not appear more than once then return True
    # in this context returning true, neans that the string is an isogram
    return True