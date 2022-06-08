class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<2:
            return nums[0]
        else:
            i=0
            while(i+1<len(nums)):
                if nums[i] != nums[i+1]:
                    return nums[i]
                else:
                    i+=2
        return nums[len(nums)-1]
