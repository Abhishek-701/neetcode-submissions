class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(0,len(nums)):
            d[nums[i]] = d.get(nums[i],0) + 1
            if d[nums[i]] > 1:
                return True
        return False

