# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

def longest(a1, a2):
    a1 = sorted(a1)
    a2 = sorted(a2)
    # your code
    
    chars = set(a1) | set(a2)
    print(''.join(sorted(chars)))
    chars = ''.join(str(sorted(chars)))
    print(chars)
    result = ''.join(sorted(chars))
    
longest("aretheyhere", "yestheyarehere"), "aehrsty"