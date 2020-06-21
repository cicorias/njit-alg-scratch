class myDictionary:
    def __init__(self, n):      # n is the size of the dictionary
        self.dict = [None]*n
        self.n = n

    def keySearch(self, key):

        # calulate the address of key, based on the simple hashing function
        addr = key % self.n
        if self.dict[addr] is None:
            return False

        # if the list in addr is initialized, then do linear search in it,
        # #using Python's native search
        if key in self.dict[addr]:
            return True
        else:
            return False

    def keyInsert(self, key):

        addr = key % self.n

        # no collision case
        if self.dict[addr] is None:
            self.dict[addr] = [key]    # initialize a list
            return

        # handling collision by appending list
        # insert only if not inserted before
        if not(key in self.dict):             # this does a linear search
            print('collision on key1: {}  key2: {}  with hash: {}'
                .format(self.dict[addr], key, addr))
            self.dict[addr].append(key)

    def keyDelete(self, key):
        addr = key % self.n

        s = self.dict[addr]
        if s is not None and len(s) == 1:
            self.dict[addr] = None
        elif s is not None and len(s) > 1:
            for i in range(len(s)):
                if key == s[i]:
                    s[i] = s[len(s) - 1] #swap with end
                    self.dict[addr] = s[0:len(s) - 1] #set to start minus end
            
        


#
#
#
#
#

md = myDictionary(11)
md.keyInsert(2)

md.keyInsert(3)

md.keyInsert(14)  # first collision

md.keyInsert(25)

md.keyInsert(36)
print(md.dict)


md.keyDelete(25)
print('deleted 25: {}'.format(md.dict))

md.keyDelete(2)
print('deleted 2: {}'.format(md.dict))
