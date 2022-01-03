from Node import Node

class DoubleLinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        
        self.head.next=self.tail
        self.tail.prev=self.head
        
        self.d_size=0

    def empty(self):
        if self.d_size==0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add_first(self, data):
        new_node=Node(data)
        
        new_node.next=self.head.next
        new_node.prev=self.head

        self.head.next.prev=new_node
        self.head.next=new_node

        self.d_size+=1

    def add_last(self, data):
        new_node=Node(data)

        new_node.prev=self.tail.prev
        new_node.next=self.tail

        self.tail.prev.next=new_node
        self.tail.prev=new_node

        self.d_size+=1

    def insert_after(self, data, node):
        new_node=Node(data)

        new_node.next=node.next
        new_node.prev=node

        node.next.prev=new_node
        node.next=new_node

        self.d_size+=1

    def insert_before(self, data, node):
        new_node=Node(data)

        new_node.prev=node.prev
        new_node.next=node

        node.prev.next=new_node
        node.prev=new_node

        self.d_size+=1

    def search_forward(self, target):
        cur=self.head.next
        
        while cur is not self.tail:
            if cur.data==target:
                return cur
            cur=cur.next
        return None

    def search_backward(self, target):
        cur=self.tail.prev
        while cur is not self.head:
            if cur.data==target:
                return cur
            cur=cur.prev
        return None
        
    def delete_first(self):
        if self.empty():
            return
        self.head.next=self.head.next.next
        self.head.next.prev=self.head

        self.d_size-=1

    def delete_last(self):
        if self.empty():
            return
        self.tail.prev=self.tail.prev.prev
        self.tail.prev.next=self.tail

        self.d_size-=1

    def delete_node(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

        self.d_size-=1

def show_list(dlist):
    print('data size : {}'.format(dlist.size()))
    cur=dlist.head.next
    while cur is not dlist.tail:
        print(cur.data, end="  ")
        cur=cur.next
    print()