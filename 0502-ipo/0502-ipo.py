'''
When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap =[]
        maxheap= []
        

        
        for i,ele in enumerate(capital):
            heappush(minheap,[ele,i])
            
        # print(minheap,"init")
        
        for j in range(k):
            while minheap and w>=minheap[0][0]:
                _,idx = heappop(minheap)
                heappush(maxheap,-profits[idx])
                

            
            if maxheap:
                top=-heappop(maxheap)
                w+=top
        return w
                
                
                