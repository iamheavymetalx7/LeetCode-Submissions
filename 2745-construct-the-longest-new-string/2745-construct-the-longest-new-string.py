class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x!=y:
            return (z+min(x,y)*2+1)*2
        return (z+x*2)*2