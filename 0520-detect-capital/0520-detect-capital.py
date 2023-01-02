class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        arr=[]
        cnt=0
        for i in range(len(word)):
            if word[i].isupper():
                cnt+=1
                arr.append(i)
                
        if cnt==len(word):
            return True
        elif cnt==0:
            return True
        elif cnt==1 and arr[0]==0:
            return True
        else:
            return False
        