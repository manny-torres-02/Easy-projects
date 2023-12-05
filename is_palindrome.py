# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         original = str(x) 
        
#         new_number = str(original)[::-1]
        
#         if original == new_number:
#             print(True)
#             return True
#         else: 
#             print(False)
#             return False
        
# testing = Solution()
# testing.isPalindrome(12217)

class Solution2: 
    def isPalindrone(self, x: int) -> bool:
        reversed = 0 
        test_number = x 
        
        while test_number != 0:
            current_digit  = test_number % 10 
            reversed = reversed * 10 + current_digit
            test_number = test_number // 10
        print(reversed)
        
        if reversed == x:
            print(True)
            return True
        else:  
            print(False)
            return False
        
test2 = Solution2()
test2.isPalindrone(1221)