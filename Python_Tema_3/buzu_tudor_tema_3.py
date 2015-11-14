#Tema 3
from datetime import datetime
from bs4 import BeautifulSoup
import requests

class Book(object):
    def __init__(self, title, author, publisher, language, isbn, quantity, pages, price, publication_date, category):
            self.title = title
            self.author = author
            self.publisher = publisher
            self.language = language
            self.isbn = isbn
            self.quantity = quantity
            self.pages = pages
            self.price = price
            self.publication_date = publication_date
            self.category = category
            
            
class BookStore(object):
    def __init__(self, url):
            self.books = [] 
            self.url = url
            self.res = requests.get(self.url)
            self.bs = BeautifulSoup(self.res.content, 'lxml')
            
            self.a = self.bs.find_all('item')              
            for ob in self.a:
                self.books += [Book(ob.find().text, ob.find('author').text, ob.find('publisher').text,\
                                    ob.find('language').text, ob.find('isbn').text, int(ob.find('quantity').text),\
                                    int(ob.find('pages').text), float(ob.find('price').text),\
                                    datetime.strptime(ob.find('pub-date').text, '%Y-%m-%d'), ob['cat'])]
                        
            self.b = self.bs.find_all('category')
            self.categories = { ob['code'] : ob['desc'] for ob in self.b }  
            
                 
    def search(self, b_title, ignore_case = False):
        self.sol = [ x for x in self.books if (b_title in x.title) or (ignore_case and b_title.lower() in  x.title.lower()) ]
        return self.sol[0] if len(self.sol) else None
        
    
    def buy(self, book, b_quantity):
        if isinstance(book, Book):
            book.quantity -= b_quantity
            return b_quantity * book.price
        return 0
        
    
    def order_by(self, atribut):
        self.books = sorted(self.books, key=lambda x : getattr(x, atribut))
        
    
    def total_cost(self):
        return float(sum([x.price * x.quantity for x in self.books]))
     
    
    total_cost = property(total_cost)
    
    
    def categories_count(self):
        return { b : sum([1 for x in self.books if x.category == a]) for (a, b) in self.categories.items()  } 
    
    
    categories_count = property(categories_count) 


# Functie ajutatoare folosita la testare.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '{0} got: {1}, expected: {2}'.format(prefix, got, expected)


# Functia care testeaza rezultatele.
def main():
    bs = BookStore('https://today.java.net/images/2007/04/books.xml')
    test(len(bs.books), 6)
    book = bs.books[0]
    test(book.title, 'Pride and Prejudice')
    test(book.author, 'Jane Austen')
    test(book.publisher, 'Modern Library')
    test(book.language, 'English')
    test(book.isbn, '0679601686')
    test(book.quantity, 187)
    test(book.pages, 352)
    test(book.price, 4.95)
    test(book.category, 'MMP')
    test(book.publication_date, datetime(2002, 12, 31))

    test(bs.search('affair'), None)
    test(bs.search('affair', ignore_case=True), bs.books[-1])

    book = bs.search('Height')
    test(bs.buy(book, 2), 13.16)
    test(bs.books[1].quantity, 111)
    test(bs.buy(u'Jude the Obscure', 2), 0)

    bs.order_by('title')
    test([b.title for b in bs.books],
         [u'Jude the Obscure',
          u'Pride and Prejudice',
          u"Tess of the d'Urbervilles",
          u'The Big Over Easy',
          u'The Eyre Affair',
          u'Wuthering Heights'])
    bs.order_by('publication_date')
    test([b.publication_date.year for b in bs.books],
         [1984, 1998, 2002, 2002, 2003, 2005])
    bs.order_by('pages')
    test([b.pages for b in bs.books],
         [346, 352, 384, 430, 480, 528])

    test(bs.total_cost, 6964.59)

    test(len(bs.categories), 3)
    test(bs.categories_count,
         {u'Hard Cover': 1, u'Paperback': 4, u'Mass-market Paperback': 1})

if __name__ == '__main__':
    main()
