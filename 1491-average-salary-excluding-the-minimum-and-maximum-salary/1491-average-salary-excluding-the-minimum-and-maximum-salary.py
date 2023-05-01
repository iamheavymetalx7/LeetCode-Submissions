class Solution:
    def average(self, salary: List[int]) -> float:
        maxi=max(salary)
        mini=min(salary)
        
        s=sum(salary)
        n=len(salary)
        
        
        return (s-maxi-mini)/(n-2)