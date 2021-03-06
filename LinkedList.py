from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data[0] == item:
        return counter
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1



  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  # Change this to match instructions
  def print_nodes(self):
    current = self.head
    
    if current != None:
    #   print('The linked list is empty.')   
      for i in range(self.length()):
        print(f'{current.data[0]}: {current.data[1]}')
        current = current.next

  def put(self, item):
    curr = self.head
    if curr:
      while curr:
        if curr.data[0] == item:
          curr.data = (curr.data[0], curr.data[1] + 1)
          return
        curr = curr.next
    self.append((item, 1))
		