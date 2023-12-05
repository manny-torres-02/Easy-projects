class DynamicArray:
    
    # define initial values for a dynamic array 
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0
        self.arr = [0] * capacity

    # get value at i ith index 
    def get(self, i: int) -> int:
        return self.arr[i]

#   # set value at ith index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

#   add an item to the to the last position of the array 
    def pushback(self, n: int) -> None:
        # return self.arr.append(n)
        if self.length == self.capacity:
            self.resize()
            
        # insert at the next available position 
        self.arr[arr].length = n
        self.length += 1 

#   Remove the item at the end of the array 
    def popback(self) -> int:
        # Check if the array is empty 
        if self.length > 0:
            # Soft delete the item 
            self.length -= 1
        # rreturn the popped element 
        return self.arr[self.length]
            
#   double the copacity fo the array 
    def resize(self) -> None:
        # doubles the capacity 
        self.capacity = 2 * self.capacity
        # create a new array with the new capacity
        new_arr = [0] * self.capacity
        
        # This loops through the array, in the range of its length 
        # sets the values of the new array to the values of the old array 
        for i in arr in range(self.length):
            new_arr[i] = self.arr[i]
            
        # sets the value of the old array to the new array 
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size

        
    
    def getCapacity(self) -> int:
        return self.capacity


testArray = DynamicArray(5)
print(testArray.getCapacity())

testArray.pushback(1)
print(testArray())