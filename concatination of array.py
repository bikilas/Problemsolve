class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()  # Create a copy of nums
        ans.extend(nums)   # Extend ans with the elements of nums
        return ans
