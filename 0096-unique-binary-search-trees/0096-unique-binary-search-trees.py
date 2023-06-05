class Solution:
    def numTrees(self, n: int) -> int:
        
        numTree=[1]*(n+1)
        
        for node in range(2,n+1):
            cnt=0
            for root in range(1,node+1):
                left = root-1
                rigt = node-root
                cnt+= numTree[left]*numTree[rigt]
            numTree[node] =cnt
            
        return numTree[n]
        