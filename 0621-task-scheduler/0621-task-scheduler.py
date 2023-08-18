class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cf = Counter(tasks)
        
        maxi = max(cf.values())
        
        arr=[v for v in cf.values()]
        
        cnt_maxi = arr.count(maxi)
        
        ans = max(len(tasks), (n+1)*(maxi-1)+cnt_maxi)
        return ans