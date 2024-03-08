class Solution(object):
    def myAtoi(self, s):
        if not s:
            return 0

        s=s.lstrip()
        if not s or (not s[0].isdigit() and s[0] not in ['+','-']):
            return 0

        if s[0]=='-':
            sign=-1
            i=1
        elif s[0]=='+':
            sign=1
            i=1
        else:
            sign=1
            i=0

            

        result=0
        for char in s[i:]:
            if char.isdigit():
                result=result*10 + int(char)
            else:
                break
        result=result*sign

        INT_MAX=2**31-1
        INT_MIN=-2**31
        if result<INT_MIN:
            return INT_MIN
        if result>INT_MAX:
            return INT_MAX
            
        return result


        """
        :type s: str
        :rtype: int
        """
        