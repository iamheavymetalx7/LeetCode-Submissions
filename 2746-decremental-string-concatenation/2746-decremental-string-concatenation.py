class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        
        
        n=len(words)
        
        @cache
        def recur(idx,fir,last):
            if idx>=n:
                return 0
            
            join1,join2 =0,0
            
            join1 = len(words[idx])+(-1 if last==words[idx][0] else 0)+recur(idx+1,fir,words[idx][-1])
            join2 = len(words[idx])+(-1 if fir==words[idx][-1] else 0)+recur(idx+1,words[idx][0],last)
            
            return min(join1,join2)
        
        val =recur(1,words[0][0],words[0][-1])
        return val+len(words[0])