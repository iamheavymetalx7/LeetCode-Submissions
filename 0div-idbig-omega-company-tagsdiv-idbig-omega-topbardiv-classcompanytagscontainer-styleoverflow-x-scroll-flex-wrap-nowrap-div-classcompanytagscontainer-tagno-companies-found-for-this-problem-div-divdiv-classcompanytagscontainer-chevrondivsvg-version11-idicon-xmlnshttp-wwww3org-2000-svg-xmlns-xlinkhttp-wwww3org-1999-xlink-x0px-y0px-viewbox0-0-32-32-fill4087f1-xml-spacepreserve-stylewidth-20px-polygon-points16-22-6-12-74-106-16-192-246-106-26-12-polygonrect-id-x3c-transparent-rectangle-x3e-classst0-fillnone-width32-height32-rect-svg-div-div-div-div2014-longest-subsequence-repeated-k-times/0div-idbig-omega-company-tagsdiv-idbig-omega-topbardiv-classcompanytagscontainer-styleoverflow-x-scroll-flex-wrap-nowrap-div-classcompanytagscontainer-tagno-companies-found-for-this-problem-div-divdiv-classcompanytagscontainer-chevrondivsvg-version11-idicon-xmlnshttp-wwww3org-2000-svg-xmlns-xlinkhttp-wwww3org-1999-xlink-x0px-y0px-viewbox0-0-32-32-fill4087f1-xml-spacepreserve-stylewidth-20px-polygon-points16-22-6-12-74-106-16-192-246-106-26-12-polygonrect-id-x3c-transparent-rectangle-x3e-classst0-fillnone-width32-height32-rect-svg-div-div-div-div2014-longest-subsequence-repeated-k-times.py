class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq= [0]*(26)
        for i,x in enumerate(s):
            freq[ord(x)-ord('a')]+=1
        
        valid_candidates =[chr(i+97) for i,x in enumerate(freq) if x>=k]
        
        
        
        q=deque()
        q.append("")
        
        def fn(ss):
            i,cnt=0,0
            
            for ch in s:
                if ss[i]==ch:
                    i+=1
                    if i==len(ss):
                        cnt+=1
                        if cnt==k:
                            return True
                        i=0
            return False
        ans=""
        while q:
            node = q.popleft()
            for cand in valid_candidates:
                new = node+cand
                if fn(new):
                    ans= new
                    q.append(new)
        return ans
                