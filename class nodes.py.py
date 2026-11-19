class Node:
    def __init__(self, data):
        self.data = data          
        self.next = None

class SinglyLinkedList :
    def __init__(self):
        self.head = None      
        self.tail = None       
        self._size = 0
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail = new_node    

        else:
            self.tail.next=new_node
            self.tail=new_node
        self._size+=1
    def __iter__(self):
        current=self.head
        while current is not None:
            yield current.data
            current=current.next
    def insert_at(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if index == self._size:
            self.append(data)
            return
        new_node = Node(data)
        if index==0:
            new_node.next=self.head
            self.head=new_node
            self._size+=1
            return
        prev = self.head                 
        for i in range(index - 1):       
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node
        self._size+=1
    def delete_at(self, index):
        if index<0 or index>=self._size:
            raise IndexError("Index out of bounds")
        if index == 0:
            removed = self.head
            self.head = self.head.next
            removed.next = None
            if self.head is None:
                self.tail = None
            self._size -= 1
            return removed.data
        prev = self.head
        for i in range(index - 1):
            prev = prev.next
        removed = prev.next
        prev.next = removed.next
        if removed is self.tail:
            self.tail = prev
        removed.next = None
        self._size -= 1
        return removed.data
class TextEditor:
    def __init__(self):
        self.lines = SinglyLinkedList()    
        self.undo_stack = []              
        self.redo_stack = []               

    def add_line(self, text):
        index = self.lines._size           
        self.lines.append(text)
        self.undo_stack.append(("insert", index, text))
        self.redo_stack.clear() 
    def insert_line(self, index, text):
        self.lines.insert_at(index, text)           
        self.undo_stack.append(("insert", index, text))
        self.redo_stack.clear()
    def delete_line(self, index):
        text = self.lines.delete_at(index)            
        self.undo_stack.append(("delete", index, text))  
        self.redo_stack.clear()
    def undo(self):
        if not self.undo_stack:                      
            return
        record = self.undo_stack.pop()               
        action, index, text = record

        if action == "insert":
            self.lines.delete_at(index)           
        else:
            self.lines.insert_at(index, text)     
        self.redo_stack.append(record)               

    def redo(self):
        if not self.redo_stack:                       
            return
        record = self.redo_stack.pop()
        action, index, text = record

        if action == "insert":
            self.lines.insert_at(index, text)        
        else:
            self.lines.delete_at(index)              

        self.undo_stack.append(record)              

    def show(self):
        for number, text in enumerate(self.lines, 1):
            print(f"{number}: {text}")
        


ed = TextEditor()
ed.add_line("A"); ed.add_line("B"); ed.add_line("C")
ed.delete_line(1)    
ed.undo()              
ed.undo()              
ed.redo()              
ed.add_line("D")      
ed.redo()              
ed.show()
