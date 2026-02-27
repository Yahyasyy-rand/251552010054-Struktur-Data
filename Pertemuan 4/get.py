kontak = {'Fadhil':'08123456789', 'Andi':'08234567890'}
print("nomor Fadhil:", kontak.get('Fadhil'))
print("nomor yang tidak ada:", kontak.get('Cici', 'Tidak ditemukan'))