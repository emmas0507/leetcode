class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class MinHeap(object):
    def __init__(self):
        self.array = [None]

    def insert(self, value):
        self.array = self.array + [value]
        index = len(self.array) - 1
        while index > 1:
            if self.array[index] < self.array[index // 2]:
                tmp = self.array[index]
                self.array[index] = self.array[index // 2]
                self.array[index // 2] = tmp
                index = index // 2
            else:
                break

    def get_min(self):
        return self.array[1]

    def extract_min(self):
        minval = self.array[1]
        self.array[1] = self.array[-1]
        self.array = self.array[:(-1)]
        index = 1
        while index < len(self.array) / 2:
            leftchild = index * 2
            rightchild = index * 2 + 1
            if rightchild >= len(self.array):
                if self.array[index] > self.array[leftchild]:
                    tmp = self.array[leftchild]
                    self.array[leftchild] = self.array[index]
                    self.array[index] = tmp
                    index = leftchild
                    print('left child to root, array is {}'.format(self.array))
            else:
                if self.array[index] > self.array[leftchild] and self.array[rightchild] >= self.array[leftchild]:
                    tmp = self.array[leftchild]
                    self.array[leftchild] = self.array[index]
                    self.array[index] = tmp
                    index = leftchild
                    print('left child to root, array is {}'.format(self.array))
                elif self.array[index] > self.array[rightchild] and self.array[leftchild] > self.array[rightchild]:
                    tmp = self.array[rightchild]
                    self.array[rightchild] = self.array[index]
                    self.array[index] = tmp
                    index = rightchild
                    print('right child to root, array is {}'.format(self.array))
            # if self.array[index] <= self.array[leftchild] and \
            #         ((rightchild < len(self.array) and self.array[index] <= self.array[rightchild]) or (rightchild >= len(self.array))):
            #         print('break')
            #         break
            # if self.array[leftchild] < self.array[index]:
            #     tmp = self.array[leftchild]
            #     self.array[leftchild] = self.array[index]
            #     self.array[index] = tmp
            #     index = leftchild
            #     print('left child to root, array is {}'.format(self.array))
            # if rightchild < len(self.array) and self.array[rightchild] < self.array[index]:
            #     tmp = self.array[rightchild]
            #     self.array[rightchild] = self.array[index]
            #     self.array[index] = tmp
            #     index = rightchild
            #     print('right child to root, array is {}'.format(self.array))
        return minval


def nth_highest_salary(input_list, K):
    mh = MinHeap()
    for v in input_list[:K]:
        mh.insert(v)
        print('val is {} and mh is {}'.format(v, mh.array))
    for v in input_list[K:]:
        if v > mh.get_min():
            mh.extract_min()
            print('extract min and mh is {}'.format(mh.array))
            mh.insert(v)
            print('val is {} and mh is {}'.format(v, mh.array))
    return mh.get_min()

input_list = [4, 3, 2, 1, 5, 6, -1, 8, 9]
K = 4
print(nth_highest_salary(input_list, K))
# mh = MinHeap()
# mh.insert(4)
# mh.insert(3)
# mh.insert(2)
# mh.insert(1)
# mh.extract_min()
# mh.insert(5)
# mh.insert(6)
# mh.insert(-1)
