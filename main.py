from add_book import add_book
from issue_book import issue_book
from return_book import return_book
from utils import library

def show_books():
    for id, info in library.items():
        status = 'available' if info['available'] else ' issued'
        print(f"{id}-{info['title']} ({status})")

while True:
    print("1. show books")
    print("2. Add books")
    print("3. Issue books")
    print("4. Return books")
    print("5. Exit books")

    ch = input('enter choice')

    if ch =='1':
        show_books()
    elif ch == '2':
        add_book()
    elif ch == '3':
        issue_book()
    elif ch == '4':
        return_book()
    elif ch == '5':
        break
    else:
        print("wrong choice")