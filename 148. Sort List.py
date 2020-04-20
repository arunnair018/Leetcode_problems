class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        ptr = slow = fast = head
        while fast and fast.next:
            ptr = slow
            slow = slow.next
            fast = fast.next.next
        ptr.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left,right)
    
    def merge(self, left, right):
        merge_list = ListNode(0)
        ptr = merge_list
        while left and right:
            if left.val <= right.val:
                ptr.next = left
                left = left.next
            elif left.val > right.val:
                ptr.next = right
                right = right.next
            ptr = ptr.next
        ptr.next = left or right
        return merge_list.next
