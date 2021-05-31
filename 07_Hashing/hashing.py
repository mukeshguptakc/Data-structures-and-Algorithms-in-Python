class Pair:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

class HashTable:
    SIZE = 100
    def __init__(self):
        self.SLOTS = HashTable.SIZE
        self.table = [None] * self.SLOTS
        for i in range(0, len(self.table)):
            self.table[i] = list()

    def put(self, key, value):
        # 1. decide the slot of the table in which value is to be added.
        index = hash(key) % self.SLOTS
        # 2. traverse the bucket and check if key is already present in that slot/bucket.
        for p in self.table[index]:
            if key == p.key:
                # 3. overwrite value, if key already present.
                p.value = value
                return
        # 4. if key is not present, add/append key-value pair in that slot/bucket.
        pair = Pair(key, value)
        self.table[index].append(pair)

    def get(self, key):
        # 1. decide the slot of the table in which entry can be found.
        index = hash(key) % self.SLOTS
        # 2. traverse the bucket and check if key is present in that slot/bucket.
        for p in self.table[index]:
            # 3. if key exists return the value.
            if key == p.key:
                return p.value
        # 4. if not found return None.
        return None


if __name__=="__main__":
    ht = HashTable()
    ht.put(2203, "Analyst")
    ht.put(4605, "Developer")
    ht.put(7401, "Quality Assurance")
    ht.put(5998, "HR")
    ht.put(6401, "CEO")
    ht.put(7101, "Manager")
    ht.put(6401, "Director")

    key = 6401
    res = ht.get(key)
    print(str(key) + " ->" + str(res))
    key = 7401
    res = ht.get(key)
    print(str(key) + " ->" + str(res))

"""
python 07_Hashing/hashing.py
6401 ->Director
7401 ->Quality Assurance
"""