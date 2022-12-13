class Solution:
    def recursion(self,candidates, target, ans,ds,index):

        if index>=len(candidates):
            if target==0 and ds not in ans:
                ans.append(ds.copy())
            return

# Note - I have used ds.copy() to avoid overwriting of array due to reference. You can refer to Python Deep Copy and Shallow Copy concept for more info


        
        if candidates[index]<=target:
            ds.append(candidates[index])
            self.recursion(candidates,target-candidates[index],ans,ds,index)
            ds.pop()
        self.recursion(candidates,target,ans,ds,index+1)
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        self.recursion(candidates,target,ans,ds,0)
        return ans