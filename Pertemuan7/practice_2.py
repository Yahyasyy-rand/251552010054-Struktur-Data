from class_node import Node

def print_linked_list(node):
    while node:
        next_id = id(node.next) if node.next else None
        print(f"[{node.data}]| next: {next_id}] -->", end="")
        node = node.next
    print("NULL")

a = Node("Roti")
b = Node("Cireng")
c = Node("Cakwe")

a.next = b
b.next = c

print_linked_list(a)