class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store {number: index}
        prevMap = {} 
        
        for i, n in enumerate(nums):
            # What number do we need to reach the target?
            diff = target - n 
            
            # Check if we've already seen that needed number
            if diff in prevMap:
                return [prevMap[diff], i]
            
            # If not, add the current number and its index to the dictionary
            prevMap[n] = i