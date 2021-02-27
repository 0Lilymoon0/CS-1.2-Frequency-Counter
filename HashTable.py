from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  def create_arr(self, size):
     
    temp = []
    for i in range(size):
      temp.append(LinkedList())
    return temp

  def hash_func(self, key):
    
    key_length = len(key)

    index = key_length % self.size

    return index


  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):

    # Calculated the index
    index = self.hash_func(key) 

    # we got the linked list we need to insert into
    ll = self.arr[index]

    # we check if it already exists in the linked list
    index_in_linkedlist = ll.find(key)

    # If not found
    if index_in_linkedlist == -1:
      item = (key, value)
      ll.append(item)
    else:
      self.arr[index].put(key)

  # 4️⃣ TODO: Modify print_nodes() in LinkedList class to be formatted correctly (see instructions)

  def print_key_values(self):
    for ll in self.arr:
      ll.print_nodes()