from class_node import Node

a = Node("Bakwan")
b = Node("Tahu Goreng")
c = Node("Risol")

a.next = b
b.next = c

current = a
while current:
    print(f"Node @ {id(current)} | data: {current.data} | Next: {id(current.next) if current.next else None}")
    current = current.next