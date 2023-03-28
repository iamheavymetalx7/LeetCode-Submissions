class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        

        n=len(nums)
        ans=[]
        if not nums:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        
        left=0
        for i in range(1,n):
            # print(nums[i],nums[i-1])
            # print(left,i)
            if nums[i]-nums[i-1]<=1:
                continue
                
            else:
                if i-left>1:
                    # print(str(left)+"->"+str(i-1))
                    ans.append(str(nums[left])+"->"+str(nums[i-1]))
                else:
                    # print(str(nums[left]),"here222")
                    ans.append(str(nums[left]))

                left=i
        if i-left>=1:
            ans.append(str(nums[left])+"->"+str(nums[i]))
        else:
            ans.append(str(nums[left]))
        return ans
                
                
        