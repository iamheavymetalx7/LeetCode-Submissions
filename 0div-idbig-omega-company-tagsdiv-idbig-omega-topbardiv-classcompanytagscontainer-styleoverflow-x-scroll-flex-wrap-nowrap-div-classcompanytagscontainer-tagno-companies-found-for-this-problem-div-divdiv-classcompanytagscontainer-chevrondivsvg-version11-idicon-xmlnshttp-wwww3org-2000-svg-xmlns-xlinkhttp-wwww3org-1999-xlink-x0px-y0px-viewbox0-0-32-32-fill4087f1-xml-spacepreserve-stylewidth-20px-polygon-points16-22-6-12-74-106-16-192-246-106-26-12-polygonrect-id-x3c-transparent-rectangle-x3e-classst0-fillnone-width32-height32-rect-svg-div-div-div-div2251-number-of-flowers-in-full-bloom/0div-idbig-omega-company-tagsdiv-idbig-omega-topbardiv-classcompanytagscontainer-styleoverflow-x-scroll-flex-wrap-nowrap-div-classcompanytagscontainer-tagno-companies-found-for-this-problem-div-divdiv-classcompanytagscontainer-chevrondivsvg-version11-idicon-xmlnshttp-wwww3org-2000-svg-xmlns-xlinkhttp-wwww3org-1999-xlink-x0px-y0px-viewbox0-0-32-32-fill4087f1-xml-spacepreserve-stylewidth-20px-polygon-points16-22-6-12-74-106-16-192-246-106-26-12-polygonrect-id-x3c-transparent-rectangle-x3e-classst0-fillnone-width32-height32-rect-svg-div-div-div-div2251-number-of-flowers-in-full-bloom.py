from sortedcontainers import SortedDict
class Solution:
    def fullBloomFlowers(self, flowers, people) -> List[int]:
        diff = defaultdict()
        diff[0]=0
        
        for s,e in flowers:
            if s in diff:
                diff[s]+=1
            else:
                diff[s]=1
            if (e+1) in diff:
                diff[e+1]-=1
            else:
                diff[e+1]=-1
        
        positions =[]
        prefix =[]
        curr=0
        
        for key in sorted(diff.keys()):
            positions.append(key)
            curr+=diff[key]
            prefix.append(curr)
        
        ans =[]
        
        
        for person in people:
            i = bisect_right(positions,person)-1
            ans.append(prefix[i])
        return ans