class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(head):
    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev
