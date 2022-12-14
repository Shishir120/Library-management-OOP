class Library:

    def __init__(self, listofbooks, library_name) -> None:
        self.listofbooks = listofbooks
        self.library_name = library_name

    @property
    def Displaybook(self):
        # To display the available books
        return self.listofbooks

    def Lendbook(self):
        print("Which book do you want to lend?")
        for i in enumerate(kinglibrary.Displaybook.values()):   #To display index along with books.
            print(i)
        
        user_book_num = int(input("Select a book number:  "))
        for index, items in enumerate(kinglibrary.Displaybook.values()): 
            if user_book_num == index:
                print(f"You have successfully lended the book {items}")
                del kinglibrary.Displaybook[items]

    @property
    def Addbook(self):
        # To add a book to the library

        print("Which book do you want to add?:")


        pass

    @property
    def Returnbook(self):
        # To return the book to the library.
        pass


# Creating an object
kinglibrary = Library({"Ram" : "You can win" , "Robert" : "Rich dad poor dad" , "Hari" : "Naruto Shippuden",\
    "Eichiro Oda" : "One Piece" , "Shyam" : "Pirates of the Caribbean"},"King's Library" )

while True:
    user_input = input(
        "press D to Display Book, L to Lend Book , A to Add Book and R Return Book \t")
    if user_input.upper() == "D":
        print(list(kinglibrary.Displaybook.values()))

    if user_input.upper() == "L":
        kinglibrary.Lendbook()
    break
