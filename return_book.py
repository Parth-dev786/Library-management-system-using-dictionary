from datetime import datetime
from utils import library,issued_books,calculate_fine

def return_book():
    book_id = input('enter book id')

    if book_id in issued_books:
        record = issued_books[book_id]
        delay = (datetime.now()-record['return_date']).days

        if delay > 0:
            fine = calculate_fine(delay)
            print(f"late fine = {fine}")
        else:
            print("returned on time")

        library[book_id]['available'] = True
        del issued_books[book_id]
    else:
        print('invalid id')
