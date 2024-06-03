class Author:
    All=[]
    def __init__(self,name):
        self.name = name
        Author.All.append(self)
    def contracts(self):
        print(Contract.All)
        return[contract for contract in Contract.All if contract.author == self]
    def books(self):
        return[contract.book for contract in self.contracts()]
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    All=[]
    def __init__(self,title,):
        self.title = title
        Book.All.append(self)
    def contracts(self):
        return[contract for contract in Contract.All if contract.book == self]
    def authors(self):
        return[contract.author for contract in self.contracts()]

class Contract:
    All=[]
    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.All.append(self)
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        if not isinstance(author,Author):
            raise Exception("Author must be of type Author")
        self._author = author
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self,book):
        if not isinstance(book,Book):
            raise Exception("Book must be of type Book")
        self._book = book
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,date):
        if not isinstance(date,str):
            raise Exception("Date must be of type str")
        self._date = date
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self,royalties):
        if not isinstance(royalties,int):
            raise Exception("Royalties must be of type int")
        self._royalties = royalties
    @classmethod
    def contracts_by_date(cls, date):
        return[contract for contract in cls.All if contract.date == date]