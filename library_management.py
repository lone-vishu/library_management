library = []
def book_details(book,idx= None):
    if idx is not None:
        print(f"\n=== Book detail {idx}==")
    print(f"Title     : {book['title'].title()}")
    print(f"Author    : {book['author'].title()}")
    print(f"Copies    : {book['copies']}")
    print("-" * 30)
while True:
    print( '\n === Library Management === \n Menu')
    print('1. Add Book \n2. View All Books \n3. Search Book \n4. Borrow Book \n5. Return Book \n6. Exit')
    try:
        menu = int(input('Choose option no. to continue'))
        
        if menu == 1:
            while True:
                book={}
                a = int(input('Type 1 to add book or type 2 to exit'))
                if a == 1:
                    book['title']= input("Enter Book's name").strip().lower()
                    book['author']= input("Enter Author's name").strip().lower()
                    book['copies']= int(input('Enter no. of copies'))
                    library.append(book)
                elif a == 2:
                    break

        elif menu == 2:
            if not library:
                print('No books available')
                continue
    
            for i, t in enumerate(library, 1):
                book_details(t,i)
        elif menu == 3:
            s = int(input('Type 1 to search by book name or type 2 to search by author name'))
            if s == 1:
                bk = input("Enter book's name").strip().lower()
                c = []
                for i in library:
                    if bk in i['title']:
                        c.append(i)
                if not c:
                    print('No results found')
                else:
                    for i,t in enumerate(c,1):
                        book_details(t,i)
            elif s == 2:
                kb = input("Enter author's name").strip().lower()
                c = []
                for i in library:
                    if kb in i['author']:
                        c.append(i)
                if not c:
                    print('No results found')
                else:
                    for i,t in enumerate(c,1):
                        book_details(t,i)

        elif menu == 4:
            br = input('Enter book to be borrowed').strip().lower()
            c = 0
            for i in library:
                if br == i['title']:
                    if i['copies']>0:
                        i['copies'] -=1
                        print('Available no. of copies:',i['copies'])
                        c +=1
                    else:
                        print('No copies available.')
            if c == 0:
                print('Enter correct book name')

        elif menu == 5:
            br = input('Enter book to be returned').strip().lower()
            c= 0
            for i in library:
                if br == i['title']:
                    i['copies'] +=1
                    print('Available no. of copies:',i['copies'])
                    c +=1
            if c == 0:
                print('Enter correct book name')

        elif menu == 6:
            exit('Goodbye! Have a bookwarming day!!')
    except ValueError:
        print('Enter valid input')
    except EOFError:
        print('Enter the option from menu')
