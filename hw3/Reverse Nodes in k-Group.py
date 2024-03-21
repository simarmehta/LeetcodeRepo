# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        # get total length first to know when to stop use slow and fast pointer for O(n/2)
        sl = head
        ft = head.next
        mid = 1
        while ft != None and ft.next != None:
            ft = ft.next.next
            sl = sl.next
            mid += 1
        #if ft == None the odd else even
        n = (mid*2)
        if ft == None:
            n -= 1
        
        possible = n/k

        curr = None # start of current k range
        st = head # pivot point
        for i in range(0,possible):
            for j in range(1,k):
                temp = st.next
                st.next = st.next.next
                if i == 0:
                    # curr = temp
                    if head != st:
                        temp.next = head
                    else:
                        temp.next = st
                    head = temp
                else:
                    temp.next = curr.next
                    curr.next = temp
            curr = st
            st = st.next

        return head
                
                
