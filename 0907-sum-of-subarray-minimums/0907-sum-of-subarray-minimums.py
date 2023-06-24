# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)  
# check comment of ks376 also
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        A = [0]+A
        res =[0]*len(A)
        st =[0] # we push indices into stack
        
        for i in range(len(A)):
            while A[st[-1]]>A[i]:
                st.pop()
            
            j= st[-1]
            # print(i,j)
            res[i] = res[j]+(i-j)*A[i]
            st.append(i)
        # print(res)
        return sum(res)%(10**9+7)
    
    
'''

def sumSubarrayMins(self, A: List[int]) -> int:
    n = len(A)
    larr = []
    st = []
     for i in range(n):
         while st and A[st[-1]] > A[i]:
             st.pop()
            
          if st:
              larr.append(st[-1])
          else:
              larr.append(-1)
          st.append(i)

     result = [0]*n # result[i] == sum of all subarrays that end at position i
     for i in range(n):
         j = larr[i]
         if j == -1:
             result[i] = (i+1)*A[i]
         else:
             result[i] = result[j] + (i-j)*A[i]

     return sum(result) % 1000000007
     
     
     
     
     
     def sumSubarrayMins(self, A: List[int]) -> int:
    n = len(A)
    st = []
    result = [0]*n  # result[i] == sum of all subarrays that end at position i
    for i in range(n):
         while st and A[st[-1]] > A[i]:
             st.pop()
            
          if st:
              j = st[-1]
              result[i] = result[j] + (i-j)*A[i]
          else:
              # j = -1
              result[i] = (i+1)*A[i]
          st.append(i)

     return sum(result) % 1000000007
     
     '''