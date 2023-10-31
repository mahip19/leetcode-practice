#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	nonzero = []
    	for i in arr:
    	    if i != 0:
    	        nonzero.append(i)
    	
    # 	print(nonzero)
    	for i in range(n - len(nonzero)):
    	    nonzero.append(0)
    # 	print(nonzero)
    	for i in range(n):
    	    arr[i] = nonzero[i]
    # 	return nonzero
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends