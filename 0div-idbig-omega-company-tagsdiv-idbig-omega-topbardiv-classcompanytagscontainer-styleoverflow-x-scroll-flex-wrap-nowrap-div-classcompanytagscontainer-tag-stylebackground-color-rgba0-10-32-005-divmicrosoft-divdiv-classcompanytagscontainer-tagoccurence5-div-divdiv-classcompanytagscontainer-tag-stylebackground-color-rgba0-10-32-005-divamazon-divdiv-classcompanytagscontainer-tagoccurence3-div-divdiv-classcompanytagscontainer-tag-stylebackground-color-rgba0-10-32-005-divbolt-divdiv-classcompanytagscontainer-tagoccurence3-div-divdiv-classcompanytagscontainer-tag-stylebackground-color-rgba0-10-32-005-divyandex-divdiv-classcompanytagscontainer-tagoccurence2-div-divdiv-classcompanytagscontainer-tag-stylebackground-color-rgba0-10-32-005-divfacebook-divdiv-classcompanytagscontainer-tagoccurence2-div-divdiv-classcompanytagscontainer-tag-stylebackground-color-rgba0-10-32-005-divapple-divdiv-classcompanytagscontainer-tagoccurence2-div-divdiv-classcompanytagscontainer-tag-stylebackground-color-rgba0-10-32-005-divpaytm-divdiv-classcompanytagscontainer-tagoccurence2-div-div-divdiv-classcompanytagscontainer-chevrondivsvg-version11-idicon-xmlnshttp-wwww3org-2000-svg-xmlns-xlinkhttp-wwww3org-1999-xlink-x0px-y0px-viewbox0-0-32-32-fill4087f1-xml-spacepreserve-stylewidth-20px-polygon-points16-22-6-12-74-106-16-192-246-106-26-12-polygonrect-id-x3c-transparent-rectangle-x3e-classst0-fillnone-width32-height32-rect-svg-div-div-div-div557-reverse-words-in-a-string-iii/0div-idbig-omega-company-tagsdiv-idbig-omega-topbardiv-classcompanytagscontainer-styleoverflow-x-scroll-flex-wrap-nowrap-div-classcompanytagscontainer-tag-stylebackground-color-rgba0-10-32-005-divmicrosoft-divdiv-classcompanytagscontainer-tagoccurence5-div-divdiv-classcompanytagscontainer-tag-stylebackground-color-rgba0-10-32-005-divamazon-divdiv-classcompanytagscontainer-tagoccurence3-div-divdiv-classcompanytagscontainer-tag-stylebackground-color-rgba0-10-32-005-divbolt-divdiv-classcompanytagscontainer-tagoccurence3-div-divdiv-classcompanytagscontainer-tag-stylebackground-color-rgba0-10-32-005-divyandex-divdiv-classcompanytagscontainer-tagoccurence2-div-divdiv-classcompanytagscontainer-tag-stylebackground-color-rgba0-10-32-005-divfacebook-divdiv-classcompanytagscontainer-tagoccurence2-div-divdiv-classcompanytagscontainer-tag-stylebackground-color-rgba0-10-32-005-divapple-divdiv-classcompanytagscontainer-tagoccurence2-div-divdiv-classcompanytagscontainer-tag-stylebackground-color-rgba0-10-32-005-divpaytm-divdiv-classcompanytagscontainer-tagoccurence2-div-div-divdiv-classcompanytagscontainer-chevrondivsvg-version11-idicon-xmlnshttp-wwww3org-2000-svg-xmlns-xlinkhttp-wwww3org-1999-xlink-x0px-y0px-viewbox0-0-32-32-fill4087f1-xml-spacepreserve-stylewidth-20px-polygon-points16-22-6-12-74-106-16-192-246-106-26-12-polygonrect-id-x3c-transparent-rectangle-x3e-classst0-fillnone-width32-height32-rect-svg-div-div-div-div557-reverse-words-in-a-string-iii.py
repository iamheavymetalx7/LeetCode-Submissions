class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        
        arr = s.split()
        new =""
        for i,ele in enumerate(arr):
            ele = ele[::-1]
            new+=ele
            if i!=len(arr)-1:
                new+=" "
        # print(new)
        return new