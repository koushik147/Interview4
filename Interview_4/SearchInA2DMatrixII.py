#Time_Complexity: O(mlogn) 
#Space_Complexity : O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix) # creating rows
        n=len(matrix[0]) # creating columns
        
        i = 0
        j = n-1
        
        while j>=0 and i<=m-1: # run until j is greater than 0 and i is less than m-1
            if matrix[i][j] == target: # if target is found
                return True
            elif matrix[i][j] < target: # if target is greater than matrix[i][j]
                i+=1 # increment i with 1
            else:
                j-=1 # decrement j with 1
                    
        return False
