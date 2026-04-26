from utils import library

def add_book():
    book_id=input("enter Book ID")
    name = input("enter book name")

    library[book_id] = {'title': name,'available':True}
    print('book Added')