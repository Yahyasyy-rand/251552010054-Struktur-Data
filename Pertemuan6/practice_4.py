class texteditor :
    def __init__(self):
        self.content = ''
        self.undo_stack = []

    def write(self, teks):
        #simpan state sebelum perubahan
        self.undo_stack.append(self.content)
        self.content += teks
        print(f'Tulis : {self.content}')

    def undo(self):
        if self.undo_stack:
            #kembalikan ke state sebelumnya
            self.content = self.undo_stack.pop()
            print(f'Undo : {self.content}')
        else:
            print('Tidak bisa di-undo lagi!')

editor = texteditor()
editor.write('Mie')
editor.write(' Ayam')
editor.write('enak abisss')
editor.undo()
editor.undo()