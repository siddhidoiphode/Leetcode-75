

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=''
        l1=len(word1)
        l2=len(word2)
        m=min(l1,l2)

        for i in range(m):
            ans+= word1[i] + word2[i]

        if l1==l2 :
            return ans
        elif l1 <l2 :
            return ans+word2[m:]
        elif l1 >l2 :
            return ans+word1[m:]









