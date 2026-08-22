class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            
            elif count != 0:
                if candidate == nums[i]:
                    count += 1
                elif candidate != nums[i]:
                    count -= 1
        
        return candidate
            
