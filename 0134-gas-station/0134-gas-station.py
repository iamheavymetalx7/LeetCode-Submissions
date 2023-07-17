class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr =0
        total =0
        
        res= 0
        
        n=len(gas)
        for i in range(n):
            ## gain[i] = gas[i]-cost[i]
            total += gas[i]-cost[i]
            curr += gas[i]-cost[i]
            
            if curr<0:
                curr=0
                res=i+1
            
        return res if total>=0 else -1