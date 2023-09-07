class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dic = defaultdict(int)
        
        for word in words:
            dic[word]+=1
        
        n=len(s)
        
        final =[]
        words_cnt = len(words)
        eachwordlength = len(words[0])
        
        
        for i in range(len(s)-(words_cnt*eachwordlength)+1):
            words_cnter = defaultdict(int)

            for j in range(words_cnt):
                
                
                stindex = i+j*eachwordlength
                
                substr = s[stindex:stindex+eachwordlength]
                if substr not in dic:
                    break
                
                words_cnter[substr]+=1
                if words_cnter[substr]>dic[substr]:
                    break
                
                if j+1 == words_cnt:
                    final.append(i)
        return final