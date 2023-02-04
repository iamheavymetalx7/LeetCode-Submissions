class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic=defaultdict(int)
        dic[" "]=0
        cnt=0
        for ele in order:
            cnt+=1
            dic[ele]=cnt
        
        for i in range(len(words)-1):
            wrd1=words[i]
            wrd2=words[i+1]
            idx1,idx2=0,0
            
            if len(wrd1)<len(wrd2):
                wrd1+=" "
            else:
                wrd2+= " "
            
            while idx1<len(wrd1) and idx2<len(wrd2):
                if dic[wrd1[idx1]]<dic[wrd2[idx2]]:
                    break
                elif dic[wrd1[idx1]]>dic[wrd2[idx2]]:
                    return False
                else:
                    idx1+=1
                    idx2+=1
        print(words)
        return True
                    
                    
        