class twoSum:
        def twoSum(self, nums: list[int], target: int) -> list[int]:
            # I need to take the first value in the array
            # Then I need to add it to the next value in the array
            # If the sum of the two values is equal to the target value
            # This will start at the first value in the array
            for i in range(len(nums)):
                # This will start at the second value in the , then moves through the entire array 
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        print("True")
                        print(nums[i], nums[j])
                        return [i,j]
            # These items will be at the level of the first for loop, so the array can be fuly traveresd. 
            print("False")
            return []

# class TwoSumDict():
#     def twoSum(self, nums: list[int], target: int) -> list[int]:



sum1 = twoSum()
sum1.twoSum([1,2,3,4,5], (7))