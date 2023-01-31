class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n=len(ages)
        arr=[[ages[i],scores[i]] for i in range(n)]
        arr.sort()
        
        print(arr)
        
        dp=[arr[i][1] for i in range(n)]
        print(dp)
        
        for index in range(n):
            for prev_index in range(index):
                if arr[index][1]>=arr[prev_index][1]:
                    dp[index]=max(dp[index],dp[prev_index]+arr[index][1])
        
        return max(dp)
                