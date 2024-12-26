class Book:

    title = 'Государь'
    author = 'Никколо Макиавелли'
    year = 1605

    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'
    
My_book = Book()

print(My_book.get_info())
