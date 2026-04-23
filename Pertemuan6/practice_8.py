from collections import deque

queue = deque()
queue.append('Yahya')
queue.append('Sudais')
queue.append('Hapis')
queue.append('Nabhan')
deque(['Yahya', 'Sudais', 'Hapis', 'Nabhan'])

print('antrian awal :', list(queue))
print('___Mulai melayani___')

nomor = 1
while queue:
    pelanggan = queue.popleft()
    print(f'[{nomor}] Melayani {pelanggan}')
    if queue:
        print(f' Antrian : {list(queue)}')
    nomor += 1

print('___Semua pelanggan telah dilayani___')