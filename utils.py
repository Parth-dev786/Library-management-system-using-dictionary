library = {'101':{'title':'python','available':True},
           '102':{'title':'C++','available':True}
           }

issued_books= {}

def calculate_fine(days):
    fine =0
    for i in range(1,days+1):
        fine+=10*i
    return fine