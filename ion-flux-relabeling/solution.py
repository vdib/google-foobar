class FullBinaryTree:
    def __init__(self, h, value=None):
        self.h = h
        self.value = value or (2 ** h)-1
        self.left = self.value - 2**(self.h-1)
        self.right = self.value -1

    def get_parent_value(self, q):
        if q > self.value or q < 1:
            return -1
        if (q == self.left) or (q == self.right):
            return self.value
        if q < self.left:
            return FullBinaryTree(self.h-1, self.left).get_parent_value(q)
        else:
            return FullBinaryTree(self.h-1, self.right).get_parent_value(q)


def solution(h, q):
    return [FullBinaryTree(h).get_parent_value(p) for p in q]
