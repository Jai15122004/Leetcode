class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count=0
        leftsum=0
        rightsum=0
        sumi=sum(nums)
        for i in range(len(nums)-1):
            leftsum+=nums[i]
            rightsum=sumi-leftsum
            if leftsum>=rightsum:
                count+=1
        return count
