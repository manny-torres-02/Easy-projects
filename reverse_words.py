def reverse_words(text):
#   Split the string into different names
    array_of_text = text.split(" ")
    reversed = []
    print(array_of_text)
    for word in array_of_text:
        # print(word[::-1])
        reversed.append(word[::-1])
        print(reversed)
        
    # reversed = reversed.strip()
    reversed_string = ' '.join(reversed)
    reversed_string = reversed_string.strip()
    print(reversed_string)
    return reversed_string
        


reverse_words('manny ate pizza today')
reverse_words('double  spaces')