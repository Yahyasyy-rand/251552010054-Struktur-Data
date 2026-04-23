def balik_string (teks) :
    stack = []

    for char in teks :
        stack.append(char)

    hasil = ''
    while stack : 

        hasil += stack.pop()

    return hasil

print(balik_string('Mie ayam'))
print(balik_string('Bakso'))
print(balik_string('Soto'))
print(balik_string('Mie goreng'))