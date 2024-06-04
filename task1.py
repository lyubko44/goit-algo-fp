class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def sort(self):
        if self.head is None or self.head.next is None:
            return
        
        sorted_list = LinkedList()
        cur = self.head

        while cur:
            next_node = cur.next
            self.sorted_insert(sorted_list, cur)
            cur = next_node
        
        self.head = sorted_list.head

    def sorted_insert(self, sorted_list, new_node):
        if sorted_list.head is None or sorted_list.head.data >= new_node.data:
            new_node.next = sorted_list.head
            sorted_list.head = new_node
        else:
            cur = sorted_list.head
            while cur.next and cur.next.data < new_node.data:
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node

def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    merged_list = LinkedList()
    merged_list.head = dummy.next

    return merged_list

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

llist.reverse()

print("\nЗв'язний список після реверсування:")
llist.print_list()

# Сортуємо зв'язний список
llist.sort()

print("\nЗв'язний список після сортування:")
llist.print_list()


list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

# Об'єднуємо два відсортованих списки
merged_list = merge_sorted_lists(list1, list2)

print("Об'єднаний відсортований список:")
merged_list.print_list()