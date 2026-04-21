class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            # Create signature: an array of 26 zeros
            count = [0] * 26

            # Count the frequency of each character in the current string
            for char in s:
                count[ord(char) - ord('a')] += 1

            # Convert the count array to a tuple so it can be a dict key
            # Append the original string to that key's list
            ans[tuple(count)].append(s)

        # ans.values() returns all the grouped lists
        return list(ans.values())