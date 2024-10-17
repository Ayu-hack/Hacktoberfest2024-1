# Method to add a node at any index
# Indexing starts from 0.
def insertAtIndex(self, data, index):
    if (index == 0):
        self.insertAtBegin(data)

    position = 0
    current_node = self.head
    while (current_node != None and position+1 != index):
        position = position+1
        current_node = current_node.next

    if current_node != None:
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
    else:
        print("Index not present")
