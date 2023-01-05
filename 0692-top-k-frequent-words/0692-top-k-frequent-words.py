from collections import defaultdict
from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #heap / priority queue
        
        n=len(words)
        dic=defaultdict(int)
        for i in range(n):
            dic[words[i]]+=1
        
        
        pq=[]
        
        for ele in dic:
            heappush(pq,[-dic[ele],ele])
        
        ans=[]
        for i in range(k):
            count, word = heappop(pq)
            ans.append(word)
        
        return ans