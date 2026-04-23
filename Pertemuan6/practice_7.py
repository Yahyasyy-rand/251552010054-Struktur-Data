from my_class_queue import martabak

q = martabak()

q.enqueue('Yahya')
q.enqueue('Lutfi')
q.enqueue('Rizwan')

print(q)
print(q.peek())

print(q.dequeue())
print(q)
print(q.size())
print(q.items_empty())