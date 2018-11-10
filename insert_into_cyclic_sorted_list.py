class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def insert_into_cyclic_list(list, target):
    head = list
    while True:
        currvalue = list.value
        nextvalue = list.next.value
        nextnextvalue = list.next.next.value
        if (currvalue <= nextvalue and nextvalue <= nextnextvalue) or (currvalue >= nextvalue and nextvalue >= nextnextvalue):
            if (target >= nextvalue and target <= nextnextvalue) or (target <= nextvalue and target >= nextnextvalue):
                print('insert value between {}, {}'.format(nextvalue, nextnextvalue))
                tmp = list.next.next
                newNode = Node(target, tmp)
                list.next.next = newNode
                return head
            else:
                list = list.next
        elif currvalue <= nextvalue and nextvalue >= nextnextvalue:
            if target >= nextvalue:
                print('insert value between {}, {}'.format(nextvalue, nextnextvalue))
                tmp = list.next.next
                newNode = Node(target, tmp)
                list.next.next = newNode
                return head
            else:
                list = list.next
        elif currvalue >= nextvalue and nextvalue <= nextnextvalue:
            if target <= nextvalue:
                print('insert value between {}, {}'.format(nextvalue, nextnextvalue))
                tmp = list.next.next
                newNode = Node(target, tmp)
                list.next.next = newNode
                return head
            else:
                list = list.next
        else:
            list = list.next
    return head

def print_list(list):
    currvalue = list.value
    print(currvalue)
    list = list.next
    while list.value != currvalue:
        print(list.value)
        list = list.next

node1 = Node(1)
node5 = Node(5, node1)
node3 = Node(3, node5)
node1.next = node3
print_list(node5)
new_list = insert_into_cyclic_list(node5, 6)
print_list(new_list)
