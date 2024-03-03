class Solution(object):
    def maxArea(self, height):
        area=0
        n=len(height)
        left,right=0,n-1
        while left<right:
            # l=min(height[left],height[right])
            # b=right-left
            x=min(height[left],height[right])*(right-left)
            if x>area:
                area=x
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
        return area
        """
        :type height: List[int]
        :rtype: int
        """
        