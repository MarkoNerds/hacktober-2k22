'''Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]'''


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
                
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -=1
        return curr

