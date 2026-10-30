class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) > 2:
            nums.sort()
            for i in range(1,len(nums)-1):
                if (nums[i-1] == nums[i]) or (nums[i+1] == nums[i]):
                    return True
        elif len(nums)==2:
            if nums[0] == nums[1]:
                return True
        return False