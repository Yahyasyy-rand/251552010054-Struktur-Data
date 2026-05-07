from class_node import Node

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head 
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_after_node(prev_node, data):
    if not prev_node:
        print("Node sebelumnya tidak boleh None")
        return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

head = Node("Jus Jeruk")
head = insert_at_beginning(head, "Es Teh")
head = insert_at_end(head, "Es Kopi")

def print_linked_list(head):
    while head:
        print(f"[{head.data}] -->", end="")
        head = head.next
    print("Null")

current = head
while current and current.data != "B":
    current = current.next
insert_after_node(current, "x")

print_linked_list(head)