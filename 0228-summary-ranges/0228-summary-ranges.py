class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        

        n=len(nums)
        ans=[]
        
#---------- boundary corner cases --------------#
        if not nums:
            return []
        if len(nums)==1:
            return [str(nums[0])]

#---------- actual code -----------#
        left=0
        for i in range(1,n):
            if nums[i]-nums[i-1]<=1:
                continue
                
            else:
                if i-left>1:
                    ans.append(str(nums[left])+"->"+str(nums[i-1]))
                else:
                    ans.append(str(nums[left]))

                left=i
#------------- what happens at the end? ---------------#
        if i-left>=1:
            ans.append(str(nums[left])+"->"+str(nums[i]))
        else:
            ans.append(str(nums[left]))
        return ans
                
                
        