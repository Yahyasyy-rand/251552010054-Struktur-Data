stack = []
print ('awal :', stack)

stack.append('Mie ayam')
stack.append('Bakso')
stack.append('Soto')
stack.append('Mie goreng')
stack.append('Mie rebus')
print ('setelah push :', stack)

top = stack [-1]
print ('peek :', top)

popped = stack.pop()
print ('dipop :', popped)
print ('stack :', stack)

print ('kosong? :', len(stack) == 0)
print ('total :', len(stack))