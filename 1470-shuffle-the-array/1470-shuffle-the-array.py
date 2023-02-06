class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)
        
        nums_ =[0]*n

        for i in range(0,n,2):
            nums_[i]=nums[i//2]

        for i in range(1,n,2):
            nums_[i]=nums[n//2+i//2]

        return(nums_)            