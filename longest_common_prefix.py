# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        print(strs)
        
        prefix = ""
        # cycle through each word  in the list
        # Do this by cycling through the index of the list
        for index in range(len(strs[0])):
            # print(strs[index])
            # cycle through word in list, but starting at the next word in the list
            for i in range(1, len(strs)):
                # print(strs[index][i])
                # if the letter is no tin the next word at the same index or position
                if index == len(strs[i]) or strs[i][index] != strs[0][index]:
                    return prefix
            # Add the letter to teh prefix 
            prefix += strs[0][index]
            print(prefix)
        return prefix
    
    
    # class Solution:
    # def longestCommonPrefix(self, strs: list[str]) -> str:
    #     print(strs)
        
    #     prefix = ""
    #     # cycle through each character in the first word
    #     for index in range(len(strs[0])):
    #         # cycle through each word in the list starting from the second word
    #         for i in range(1, len(strs)):
    #             # if the character is not in the next word at the same index or position
    #             if index == len(strs[i]) or strs[i][index] != strs[0][index]:
    #                 return prefix
    #         # add the character to the prefix
    #         prefix += strs[0][index]
    #         print(prefix)
    #     return prefix
    
testSolution =Solution()
testSolution.longestCommonPrefix(["flower","flow","flight"])     
testSolution.longestCommonPrefix(['flower', 'flower', 'flower', 'flower'])