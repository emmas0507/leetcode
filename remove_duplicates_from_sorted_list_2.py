class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def remove_duplicates_from_sorted_list_2(input):
    if input.next is None:
        return input
    curr = input.next
    curr_tail = input
    while curr is not None:
        print('curr value is {} and curr_tail.value is {}'.format(curr.value, curr_tail.value))
        if curr.value == curr_tail.value:
            curr = curr.next
        else:
            curr_tail.next = curr
            curr_tail = curr_tail.next
            curr = curr.next
    return input

def print_list(input):
    while input is not None:
        print(input.value)
        input = input.next

n5 = Node(5)
n4 = Node(4, n5)
n42 = Node(4, n4)
n2 = Node(2, n42)
n22 = Node(2, n2)
n1 = Node(1, n22)
print_list(remove_duplicates_from_sorted_list_2(n1))
