class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    
        dic={}

        for i in items1:
            dic[i[0]]=i[1]

        for j in items2:
            if j[0] in dic:
                dic[j[0]]+=j[1]
            else:
                dic[j[0]]=j[1]
        ans=[]
        print(dic)
        for i,j in dic.items():
            ans+=[[i,j]]

        ans.sort()
        return ans