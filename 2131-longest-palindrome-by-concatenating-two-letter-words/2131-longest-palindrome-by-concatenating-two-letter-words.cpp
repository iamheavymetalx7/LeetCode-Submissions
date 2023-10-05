class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        n = len(words)
        dic = defaultdict(int)
        ans = 0
        
        for i,w in enumerate(words):
            dic[w]+=1
        f=False
        for el in dic:
            new_el = el[::-1]
            if new_el in dic:
                if el[0]==el[1]:
                    if dic[el]%2:
                        f=True
                    ans+=(dic[el]//2)*4
                else:
                    mini = min(dic[el],dic[new_el])
                    ans+=mini*4
                    dic[el]-=mini
                    dic[new_el]-=mini
                    
        return ans+(2 if f else 0)