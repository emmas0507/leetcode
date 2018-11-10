class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def linked_list_cycle_2(list):
    slow = list
    fast = list
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow.value == fast.value:
            break
    if fast is None or fast.next is None:
        return None
    fast = list
    while fast.value != slow.value:
        fast = fast.next
        slow = slow.next
    return fast.value

n1 = Node(1)
n2 = Node(2, n1)
n3 = Node(3, n2)
n4 = Node(4, n3)
n5 = Node(5, n4)
n1.next = n4

print(linked_list_cycle_2(n5))
