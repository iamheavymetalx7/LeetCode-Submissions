# '''
# idea is to apply the operation on same number k times and get the final ans
# '''

class Solution:
    def maximumOr(self, A: List[int], k: int) -> int:
        res, left, = 0, 0
        
        n=len(A)
        
        right = [0] * n
        
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] | A[i + 1]
        for i in range(n):
            res = max(res, left | A[i] << k | right[i])
            left |= A[i]
        return res