class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies= [1 for _ in range(n)]
        
        heap =[]
        
        for i,ele in enumerate(ratings):
            heappush(heap,[ele,i])
            
        while heap:
            _,idx = heappop(heap)
            # print(_,idx)
            if idx+1<n and ratings[idx+1]>ratings[idx]:
                if candies[idx+1]<=candies[idx]:
                    candies[idx+1]+=(candies[idx]-candies[idx+1]+1)
            if idx-1>=0 and ratings[idx-1]>ratings[idx]:
                if candies[idx-1]<=candies[idx]:
                    candies[idx-1]+=(candies[idx]-candies[idx-1]+1)
        print(candies)
        return (sum(candies))
        