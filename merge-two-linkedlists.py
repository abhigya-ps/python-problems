class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1, l2):
    head = ListNode(0)
    ptr = head

    while l1 and l2:
        if l1.val < l2.val:
            ptr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            ptr.next = ListNode(l2.val)
            l2 = l2.next
        ptr = ptr.next

    ptr.next = l1 or l2
    return head.next

