class Book:
    def __init__(self,title:str,author:str,year:int):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self)->str:
        return f"Название книги:{self.title}, Автор:{self.author}, Год издания:{self.year}"

my_book = Book('Название','автор',2000)
print(my_book.get_info())
