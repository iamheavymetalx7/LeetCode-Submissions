class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n=len(word)
        fac=1
        arr= [0 for _ in range(n)]
        curr=0
        for i in range(len(word)):
            curr = curr*10 + int(word[i])
            curr = curr%m
            if curr%m==0:
                arr[i]=1
        return arr
            