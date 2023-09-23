class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dic=defaultdict(int)
        words = list(set(words))
        
        words.sort(key =len)
        for i,w in enumerate(words):
            dic[w]=i
        n=len(words)
        
        @cache
        def recur(i):
            cur = words[i]
            maxi =0
            for idx in range(len(cur)):
                new_w = cur[:idx]+cur[idx+1:]
                if new_w in dic:
                    maxi = max(maxi, 1+recur(dic[new_w]))
            return maxi
        
        return max(recur(i)+1 for i in range(n))