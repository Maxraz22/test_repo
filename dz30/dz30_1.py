class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[]] * self.size

    def __str__(self):
        return ''.join(map(str, self.hash_table))

    def hash_element(self, key):
        return key % self.size

    def add_element(self, key, value):
        index = self.hash_element(key)
        if not self.hash_table[index]:
            self.hash_table[index] = [key, value]
        else:
            self.hash_table[index].extend([key, value])

    def find_element(self, key):
        index = self.hash_element(key)
        if self.hash_table[index]:
            return self.hash_table[index][self.hash_table[index].index(key) + 1]
        else:
            return None

    def remove_element(self, key):
        index = hash(key) % self.size
        self.hash_table[index] = None

my_hash_table = HashTable(10)

my_hash_table.add_element(0, 'Zero')
my_hash_table.add_element(5, 'Five')
my_hash_table.add_element(7, 'Seven')
print(my_hash_table)

print(my_hash_table.find_element(5))

my_hash_table.remove_element(7)
print(my_hash_table)
