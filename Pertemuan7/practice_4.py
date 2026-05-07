from class_node import Node

def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

head = Node("martabak")
head = insert_at_end(head, "martabak manis")

def print_linked_list(head):
    while head:
        print(f"[{head.data}] -->", end="")
        head = head.next
    print("NULL")

print_linked_list(head)