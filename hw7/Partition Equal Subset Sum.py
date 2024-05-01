class Solution:
    def canPartition(a, index, target):
        # Base cases
        # means target was achieved 
        if target == 0:
            return true
        #if reached index 0, then 0th index must be the desired target which we got after 0 or couple of shrinking calls
        if index == 0:
            return (a[0] == target)
        
        take = False
        if target <= a[index]:
            # if element is take into consideration
            # shrink target when consider the curr element
            take = func(a, index-1, target - a[index])
        
        # if element is not taken into consideration for the target sum
        not_take = func(a, index-1, target)

        return take or not_take
