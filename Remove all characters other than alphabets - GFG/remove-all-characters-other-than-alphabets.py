#User function Template for python3

class Solution:
    def removeSpecialCharacter (self, S):
		#code here
		a=""
		for i in S:
		    if i.isalpha():
		        a+=i
		    else:
		        continue
		    
		if a.isalpha():
		    return a
		else:
		    return -1
		  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.removeSpecialCharacter(S))


# } Driver Code Ends