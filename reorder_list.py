class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_list(list):
    prev = list
    curr = list.next
    prev.next = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def print_list(list):
    while list is not None:
        print(list.value)
        list = list.next

def merge_list(l1, l2):
    curr_l1 = l1
    curr_l2 = l2
    while curr_l2 is not None:
        next_l1 = curr_l1.next
        next_l2 = curr_l2.next
        curr_l1.next = curr_l2
        curr_l2.next = next_l1
        curr_l1 = next_l1
        curr_l2 = next_l2
    return l1

def reorder_list(list):
    slow = list
    fast = list.next
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    print('slow point points to {}'.format(slow.value))
    second_half = slow.next
    slow.next = None
    rev_list = reverse_list(second_half)
    print('list is:')
    print_list(list)
    print('second reverse is:')
    print_list(rev_list)
    merge_list(list, rev_list)
    print('merge list is:')
    print_list(list)
    return list

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n0 = Node(0, n1)
n1_ = Node(-1, n0)

reorder_list(n1_)



