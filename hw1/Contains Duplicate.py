class Solution(object):
    def containsDuplicate(self, nums):
        s=set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        