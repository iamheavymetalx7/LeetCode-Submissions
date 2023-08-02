'''
Consider the case - [1,1,1]
We mark each of them separately [1a,1b,1c]

Consider the 2nd iteration of for loop in first recursion call:
i = 1
nums = [1a, 1b, 1c]
tempList = []
used = [0 , 0, 0]

We are not adding '1b' to the result bcz i>0 && nums[i] == nums[i-1] && !used[i-1] is true and we will move to next iteration of for loop. This ensures that permutation in which '1b' is added before '1a' are not calculated. In fact, any permutations of the form [1b, ...], [1c, ...] are not calculated.

Consider 2nd iteration of for loop in 2nd recursion call:
i = 1
nums = [1a, 1b, 1c]
tempList = [1a]
used = [1 , 0, 0]

Here, i>0 && nums[i] == nums[i-1] && !used[i-1] is false and we will add '1b' to tempList and recurs further. This ensures only 1 permutation - [1a, 1b, 1c] is calculated.

In this way are calculating only 1 permutation of duplicates [1a,1b,1c].

'''





class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)
        nums.sort()         ## must before running the backtracking functions
        used = [0]*(n)
        
        def recur(idx,arr):
            if len(arr)==n:
                ans.append(arr.copy())
            
            
            for i in range(n):
                if used[i] or (i>0 and nums[i]==nums[i-1] and not used[i-1]):continue
                    
                used[i]=True
                arr.append(nums[i])
                recur(i+1,arr)
                used[i] = False
                arr.pop()
        recur(0,[])
        return ans