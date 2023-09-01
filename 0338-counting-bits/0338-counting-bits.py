class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[0 for _ in range(n+1)]
        for i in range(n+1):
            arr[i]=i.bit_count()
        return arr