class Solution:
    def getNextIndex(self,nums,curr_index,is_Positive):
        direction = nums[curr_index]>0
        if is_Positive!=direction:
            return -1
        
        nextIndex = (curr_index+nums[curr_index])%len(nums)
        
        if nextIndex<0:
            nextIndex+=len(nums)
        
        if nextIndex==curr_index:
            return -1
        
        return nextIndex
        
        
        
        
        
        
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for index in range(len(nums)):
            is_Positive = nums[index]>=0
            
            fast,slow=index,index
            
            while True:
                fast=self.getNextIndex(nums,fast,is_Positive)
                slow=self.getNextIndex(nums,slow,is_Positive)

                if fast!=-1:
                    fast=self.getNextIndex(nums,fast,is_Positive)

                if fast==-1 or slow==-1:
                    break


                if fast==slow:
                    return True
                
        return False