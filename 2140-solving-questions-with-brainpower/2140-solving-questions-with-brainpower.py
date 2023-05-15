class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        
        
        
        @cache
        def recur(i):
            if i>=n:
                return 0
            points,jump = questions[i]
            
            
            take = points+recur(i+jump+1)
            nottake = recur(i+1)
            
            return max(take,nottake)
        
        return recur(0)
            