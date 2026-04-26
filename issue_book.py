from datetime import datetime, timedelta
from utils import library,issued_books

def issue_book():
    book_id = input('enter Book Id')

    if book_id in library and library[book_id]['available']:
        name = input('student name')
        days =int(input('days'))

        issued_books[book_id]= {'name ':name,'return_date':datetime.now()+timedelta(days=days)}

        library[book_id]['available'] = False
        print('Book issued')
    else:
        print('not Available')
