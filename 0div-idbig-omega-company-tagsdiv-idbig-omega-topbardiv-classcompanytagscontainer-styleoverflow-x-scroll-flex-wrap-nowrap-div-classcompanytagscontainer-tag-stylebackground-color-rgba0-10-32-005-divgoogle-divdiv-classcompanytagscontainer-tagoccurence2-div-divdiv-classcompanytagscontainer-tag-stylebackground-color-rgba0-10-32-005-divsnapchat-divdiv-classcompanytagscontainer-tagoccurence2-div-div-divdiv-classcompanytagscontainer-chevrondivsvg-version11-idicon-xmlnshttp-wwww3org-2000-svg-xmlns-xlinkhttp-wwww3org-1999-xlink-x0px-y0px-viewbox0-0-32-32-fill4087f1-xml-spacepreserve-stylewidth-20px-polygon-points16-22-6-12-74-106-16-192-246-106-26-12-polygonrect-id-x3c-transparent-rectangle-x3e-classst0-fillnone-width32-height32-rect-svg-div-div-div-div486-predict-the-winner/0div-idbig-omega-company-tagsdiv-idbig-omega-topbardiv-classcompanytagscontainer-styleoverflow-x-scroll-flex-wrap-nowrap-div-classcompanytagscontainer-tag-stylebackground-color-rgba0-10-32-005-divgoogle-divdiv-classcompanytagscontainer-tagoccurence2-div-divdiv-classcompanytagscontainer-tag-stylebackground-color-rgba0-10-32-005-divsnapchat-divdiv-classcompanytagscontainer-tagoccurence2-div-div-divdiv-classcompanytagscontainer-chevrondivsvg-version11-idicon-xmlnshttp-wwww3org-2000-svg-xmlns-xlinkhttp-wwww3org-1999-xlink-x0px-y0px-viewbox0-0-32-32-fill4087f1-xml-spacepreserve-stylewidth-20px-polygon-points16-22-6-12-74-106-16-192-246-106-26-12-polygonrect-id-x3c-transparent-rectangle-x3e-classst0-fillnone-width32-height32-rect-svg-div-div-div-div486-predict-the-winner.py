class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        
        n = len(nums)
        @cache
        def recur(i,j):
            if i>j:
                return 0
            score=0


            score-=(max(nums[i]+recur(i+1,j),nums[j]+recur(i,j-1)))
            return score
        
        ans = recur(0,n-1)
        # print(ans) 
        return ans<=0
    