dict = {"fast": "빠른"}


class LinkedTuple:

    def __init__(self):
        self.items = []

    def put(self, key, value):
        self.items.append((key,value))

    def get(self, key):

        for k, v in self.items:
            if k == key:
                return v


class LinkedDict:

    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].put(key,value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


my_dict = LinkedDict()
my_dict.put("test", 3)
my_dict.put("333", 7)
get = my_dict.get("test")
print(get)

