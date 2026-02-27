kontak = {'Fadhil':'08123456789'}
print("sebelum setdefault:", kontak)
kontak.setdefault('Andi','08234567890')
kontak.setdefault('Fadhil', '09000000000')
print("setelah setdefault:", kontak)