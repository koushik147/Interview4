#Time_Complexity : O(len(wordsDict))
#Space_Complexity : O(max(times(word1),times(word2)))
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        minimum=len(wordsDict)  # create minimum to length of wordsDict
        if(word1==word2):   # if both word1 and word2 are the same 
            word1List=[]    # create word1List
            for i in range(len(wordsDict)): # run until the wordsDict
                if(wordsDict[i]==word1):    # if wordsDict[i] is equal to word1
                    word1List.append(i) # append the index into word1List
            for j in range(1,len(word1List)):   # run until lenght of the list
                diff = abs(word1List[j-1]-word1List[j]) # difference between absolute value of word1List[j-1] and word1List[j]
                minimum = min(minimum,diff) # minimum difference between minimum and diff
        else:  
            word1List=[]    # create word1List 
            word2List=[]    # create word2List 
            
            for i in range(len(wordsDict)):
                if(wordsDict[i]==word1):    #If wordsDict[i] is equal to word1 
                    word1List.append(i) # append it to the word1List
                elif(wordsDict[i]==word2):  # if wordsDict[i] is equal to word2 
                    word2List.append(i) # append it to word2List
            ptr1 = 0  # create ptr1 pointer to 0
            ptr2 = 0  # create ptr2 pointer to 0
            while(ptr1 < len(word1List) and ptr2 < len(word2List)): # run unitl ptr1 is less than lenght of word1List and ptr2 is less than lenght of word2List
                diff = abs(word2List[ptr2]-word1List[ptr1]) # difference between the absolute values of word2List[ptr2] and word1List[ptr1]
                minimum = min(diff,minimum)   # minimum difference between the diff and minimum
                if(word2List[ptr2] < word1List[ptr1]):    # if the word2List[ptr2] is less than word1List[ptr1]
                    ptr2 += 1 # increment ptr2 by 1
                else:   
                    ptr1 += 1 # increment ptr1 by 1
                    
        return minimum  #Return minimum
