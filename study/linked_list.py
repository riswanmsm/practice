class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def traversal(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def insert_new_header(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False
    
    def delete_node(self, data):
        node = self.head
        prev = None
        while node:
            if node.data == data:
                break
            prev = node
            node = node.next
        if prev:
            prev.next = node.next
        else:
            self.head = node.next
    
    def delete_tail(self):
        node = self.head
        while node.next.next:
            node = node.next
        node.next = None
            
            
                
        

family = LinkedList()
husband = Node('Riswan')
wife = Node('Asna')
daughter = Node('Reeha')
son = Node('Umar')
son2 = Node('Umarr')

family.head = husband
husband.next = wife
wife.next = daughter
daughter.next = son
son.next = son2

family.insert_new_header('Mohamed Riswan')
family.delete_node('Mohamed Riswan')
family.delete_tail()

family.traversal()
print(family.search_node('Asna'))