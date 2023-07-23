#User function Template for python3

class Solution:
    def longest(self, arr, n):
        
        st=[]
        a=[-1]*(n)
        
        for i in range(n):
            while st and arr[st[-1]]<=arr[i]:
                st.pop()
            
            if not st:
                st.append(i)
                continue
            a[i]=arr[st[-1]]
            st.append(i)
        # print(a)
        return a.count(-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.longest(arr, n))

        T -= 1


if __name__ == "__main__":
    main()





# } Driver Code Ends