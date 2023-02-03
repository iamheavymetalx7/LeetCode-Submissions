from bisect import bisect_left, bisect_right
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s)<=numRows or numRows==1:
            return s
        
        string =['']*numRows
        
        index,step=0,1
        
        for x in s:
            string[index]+=x
            if index==0:
                step=1
            if index==numRows-1:
                step=-1
            index=index+step

        return "".join(string)
