class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        
        candies = [1 for _ in range(n)]
        
        for i in range(n-1):
            if ratings[i]<ratings[i+1]:
                candies[i+1]=max(candies[i+1],1+candies[i])
        
        
        for i in reversed(range(n-1)):
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i],1+candies[i+1])
        print(candies)
        return sum(candies)