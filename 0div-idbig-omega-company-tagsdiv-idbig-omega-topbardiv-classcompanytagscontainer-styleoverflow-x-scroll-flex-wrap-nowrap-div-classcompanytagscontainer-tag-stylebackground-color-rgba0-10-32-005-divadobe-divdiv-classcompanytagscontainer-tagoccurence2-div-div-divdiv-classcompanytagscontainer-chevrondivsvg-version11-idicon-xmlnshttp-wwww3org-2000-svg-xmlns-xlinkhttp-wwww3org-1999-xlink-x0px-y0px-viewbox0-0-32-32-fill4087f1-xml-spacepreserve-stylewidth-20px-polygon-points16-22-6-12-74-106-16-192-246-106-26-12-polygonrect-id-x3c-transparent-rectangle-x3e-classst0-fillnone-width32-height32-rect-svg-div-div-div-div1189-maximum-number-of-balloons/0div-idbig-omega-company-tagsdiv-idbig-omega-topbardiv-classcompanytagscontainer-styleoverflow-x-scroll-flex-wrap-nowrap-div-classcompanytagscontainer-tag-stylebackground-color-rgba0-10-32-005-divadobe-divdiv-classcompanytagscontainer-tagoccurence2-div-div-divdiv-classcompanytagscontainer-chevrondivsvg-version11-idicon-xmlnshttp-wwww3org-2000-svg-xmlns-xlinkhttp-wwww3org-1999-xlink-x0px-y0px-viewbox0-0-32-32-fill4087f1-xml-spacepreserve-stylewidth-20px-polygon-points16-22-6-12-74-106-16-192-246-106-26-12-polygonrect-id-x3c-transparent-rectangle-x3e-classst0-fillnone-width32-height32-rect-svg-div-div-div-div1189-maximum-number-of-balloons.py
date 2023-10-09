class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = Counter(text)
        # print(dic)
        ans = int(1e19)
        for x in "balloon":
            # print(x,dic[x])
            if x=="l" or x=="o":
                ans= min(ans,dic[x]//2)
                continue
            ans = min(ans,dic[x])
        return ans