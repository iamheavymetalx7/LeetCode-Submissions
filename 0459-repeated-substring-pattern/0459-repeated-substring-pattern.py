class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        n=len(s)
        
        divisors=[]
        
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                divisors.append(i)
            if n//i!=i:
                divisors.append(n//i)
        divisors.sort()
        
        print(divisors)
        
        for i,ele in enumerate(divisors):
            if ele==n:
                continue
            # print(s,s[:ele]*(n//ele))
            if s == s[:ele]*(n//ele):
                return True
        return False