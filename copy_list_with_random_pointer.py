class Node(object):
    def __init__(self, value, next=None, random=None):
        self.value = value
        self.next = next
        self.random = random

def copy_list_with_random_pointer(list):
    head = list
    while head is not None:
        new_node = Node(head.value+10, head.next, random=None)
        head.next = new_node
        head = head.next.next

    head = list
    while head is not None:
        if head.random is not None:
            head.next.random = head.random.next
        head = head.next.next

    # print_list(list)

    head = list.next
    while head.next is not None:
        # print('head is {}'.format(head.value))
        tmp_next = head.next.next
        head.next = tmp_next
        head = tmp_next
    return list.next

def print_list(list):
    while list is not None:
        if list.random is None:
            print('val is {}, random is {}'.format(list.value, None))
        else:
            print('val is {}, random is {}'.format(list.value, list.random.value))
        list = list.next

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n1.random = n5
n2.random = n3
n4.random = n1
n5.random = n2

print_list(copy_list_with_random_pointer(n1))
