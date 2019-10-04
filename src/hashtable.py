# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        index = self._hash_mod(key) 
        current_node = self.storage[index]
        new_node = LinkedPair(key, value)
        updated = False

        if current_node is None:
            self.storage[index] = new_node
        elif current_node.key == key:
            new_node.next = current_node.next;
            self.storage[index] = new_node
        else:
            while current_node.next is not None:
                if current_node.next.key == key:
                    next_value = current_node.next.next
                    new_node.next = next_value
                    current_node.next = new_node
                    updated = True
                current_node = current_node.next
            if not updated:
                current_node.next = new_node


    def remove(self, key):
        index = self._hash_mod(key)
        current_node = self.storage[index]

        if current_node.key == key:
            self.storage[index] = current_node.next
            return
        else:
            while current_node.next is not None:
                if current_node.next.key == key:
                    current_node.next = current_node.next.next
                    return
                current_node = current_node.next
        print("Key not found")

                


    def retrieve(self, key):
        currentItem = self.storage[self._hash_mod(key)]
        
        while currentItem and currentItem.key is not key:
            if currentItem.next:
                currentItem = currentItem.next
            else:
                currentItem = None
        
        if currentItem:
            return currentItem.value
        else:
            print("key not found")


    def resize(self):
        self.capacity *= 2

        copy = self.storage

        self.storage = [None] * self.capacity

        for i in copy:
            if i:
                current = i
                while current is not None:
                    self.insert(current.key, current.value)
                    current = current.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
