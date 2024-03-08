class Solution(object):
    def characterReplacement(self, s, k):
        maxlength=0
        maxcount=0
        count={}
        left=0

        for right,char in enumerate(s):
            count[char]=count.get(char,0)+1
            maxcount=max(maxcount,count[char])

            if right-left+1-maxcount>k:
                count[s[left]]-=1
                left=left+1
            
            maxlength=max(maxlength,right-left+1)
        return maxlength
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        