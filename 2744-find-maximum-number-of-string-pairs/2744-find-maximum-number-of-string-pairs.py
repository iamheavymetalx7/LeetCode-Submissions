class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set(words)
        # print(seen)
        cnt=0
        for x in words:
            if x[::-1]!=x and x[::-1] in seen:
                cnt+=1
                seen.discard(x)
                seen.discard(x[::-1])
        return cnt