#User function Template for python3

class Solution:
    
    def substring_with_atmost_k_distinct(self, s, k):
        freq = {}
        left, distinct = 0, 0
        
        count = 0
        
        for right in range(0, len(s)):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
            if freq[s[right]] == 1:
                distinct+=1
            
            while distinct > k:
                freq[s[left]]-=1
                if freq[s[left]] == 0:
                    distinct-=1
                left+=1
            
            if distinct <= k:
                count += right - left + 1
        
        return count
    
    def substrCount (self,s, k):
        # your code here
        return self.substring_with_atmost_k_distinct(s, k) - self.substring_with_atmost_k_distinct(s, k-1) 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends