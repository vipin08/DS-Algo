class Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data

class LinkList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_data = Node(new_data)
        if self.head is None:
            self.head = new_data
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_data

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def insertAfter(self,prev_node,data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteAfter(self, key):
        if self.head.data == key:
            self.head = None
            return

        temp = self.head
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if(temp is None):
            return

        prev.next = temp.next
        temp = None

    def deleteFromPosition(self, position):
        count = 1
        temp = self.head
        if position == 1:
            temp = None
            return

        while(temp is not None):
            if count == position:
                break
            prev = temp
            temp = prev.next
            count += 1

        if(temp is None):
            return

        prev.next = temp.next
        temp = None






def count_node(head):
    count = 1
    prev_c = 1
    current = head
    while(current.next != None):
        current = current.next
        count += 1
    print(count)
    while(current.prev != None):
        current = current.prev
        prev_c += 1
    print(prev_c)



if __name__ == "__main__":

    ll = LinkList()
    ll.append(2)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(48)

    ll.insertAfter(ll.head, 100)
    ll.deleteAfter(100)
    ll.deleteFromPosition(4)
    ll.print_list()
