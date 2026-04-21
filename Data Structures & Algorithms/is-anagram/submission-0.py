class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Convert strings to lists
        arr1 = list(s)
        arr2 = list(t)

        # Sort lists
        arr1.sort()
        arr2.sort()

        # Compare them
        return arr1 == arr2