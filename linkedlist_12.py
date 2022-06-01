class Node:
    def _init_(self , data = None , next = None):
        self.data = data
        self.next = next

class Linked_list:
    def _init_(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = " "
        while itr:
            llstr += str(itr.data) +"--->"
            itr  = itr.next
        print(llstr)  

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head 
        while itr.next:
            itr = itr.next 
        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_len(self):
        count = 0 
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    def remove_at(self,index):
        if index<0 or index>self.get_len():
            raise Exception("INVALID INDEX")

        if index == 0:
            self.head = self.head.next
        
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def Reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        


if _name_ =='_main_':
    ll = Linked_list()
    ll.insert_values([1,2,3,4,5,6,7,8,9,10])
    
    ll.Reverse()
    ll.print()