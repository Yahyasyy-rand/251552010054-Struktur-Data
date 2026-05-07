from class_node import Node

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

head = Node("Yahyasyy")
head = insert_at_beginning(head, "Lutfi")

def print_linked_list(head):
    while head:
        print(f"[{head.data}] -->", end="")
        head = head.next
    print("NULL")

print_linked_list(head)