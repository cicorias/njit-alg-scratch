
import collections

kv = collections.namedtuple('kv', 'key value')


class oMaxHeap:
    def __init__(self):
        self.H = []

    def heapInsert(self, x):
        n = len(self.H)
        # append in last leaf (next available position in array/list)
        self.H.append(x)

        # now bubble up x
        pos = n      # current position of bubble-up
        while True:
            if (pos == 0):
                break
            parent_pos = (pos-1)//2
            if self.H[parent_pos] < self.H[pos]:
                # copy parent value to current position
                self.H[pos] = self.H[parent_pos]
                # move x to parent's position
                self.H[parent_pos] = x
                pos = parent_pos                     # update current position
            else:
                break                                # break the bubble-up loop
        # return H


class myMaxHeap:
    def __init__(self):
        self.H = []

    def heapInsert(self, x: kv):
        n = len(self.H)
        # append in last leaf (next available position in array/list)
        self.H.append(x)

        # now bubble up x
        pos = n      # current position of bubble-up
        while True:
            if pos == 0:
                break
            parent_pos = (pos-1)//2
            if kv(*self.H[parent_pos]).key < kv(*self.H[pos]).key:
                # copy parent value to current position
                self.H[pos] = self.H[parent_pos]
                # move x to parent's position
                self.H[parent_pos] = x
                pos = parent_pos                     # update current position
            else:
                break                                # break the bubble-up loop
        # return self.H


# o = oMaxHeap()

# o.heapInsert(2)
# o.heapInsert(1)
# o.heapInsert(9)

my = myMaxHeap()
my.heapInsert((2, "2"))
my.heapInsert((1, "2"))
my.heapInsert((9, "2"))
my.heapInsert((8, "3"))
my.heapInsert((6, "2"))
my.heapInsert((5, "2"))


print(my.H)
