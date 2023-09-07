class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for i in range(31,-1,-1):
            if (left&(1<<i))!=(right&(1<<i)):
                break
            else:
                ans |= (left&(1<<i))
        return ans