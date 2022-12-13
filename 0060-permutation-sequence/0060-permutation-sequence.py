class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=1
        numbers=[]
        for i in range(1,n):
            fact=fact*i
            numbers.append(i)
        numbers.append(n)
        ans=""
        k-=1
  
        while True:
            ans+=str(numbers[k//fact])
            numbers.pop(k//fact)
            if len(numbers)==0:
                break
            k=k%fact
            fact=fact//len(numbers)
        return ans
      