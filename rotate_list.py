class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def rotate_list(list, K):
    length = 0
    head = list
    while head is not None:
        length = length + 1
        head = head.next
    K = K % length
    start = list
    end = list
    for i in range(K):
        end = end.next
    while end.next is not None:
        start = start.next
        end = end.next
    new_head = start.next
    start.next = None
    end.next = list
    return new_head

def print_list(list):
    while list is not None:
        print(list.value)
        list = list.next

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print(print_list(rotate_list(n1, 2+5)))
