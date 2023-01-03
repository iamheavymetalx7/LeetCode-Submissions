class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        arr=[]
        
        for i in range(len(strs)):
            arr.append(list(strs[i]))
        cnt=0
        for j in range(len(arr[0])):  
            string=""
            for i in range(len(arr)):
                string+=arr[i][j]
            # print(string)
            # print(''.join(sorted(string)))
            if ''.join(sorted(string))!=string:
                cnt+=1
        
        # print(cnt)
        return cnt
                
                