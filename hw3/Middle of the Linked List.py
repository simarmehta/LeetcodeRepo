class Solution(object):
    def middleNode(self, head):
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        
        x = count // 2
        temp = head
        for _ in range(x):
            temp = temp.next
        
        return temp
