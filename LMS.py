#So far so good... 12/14/2022   10:05 PM

class Library:

    def __init__(self, listofbooks, library_name) -> None:
        self.listofbooks = listofbooks
        self.library_name = library_name

    @property
    def Displaybook(self):
        # To display the available books
        return self.listofbooks


    #Method to lend books
    @property
    def Lendbook(self):
        print("Which book do you want to lend?")
        for i in enumerate(kinglibrary.Displaybook.values()):   #To display index along with books.
            print(i)
        
        user_lendbook_num = int(input("Select a book number:  "))
        for index, items in enumerate(kinglibrary.Displaybook.values()): 
            if user_lendbook_num == index:
                print(f"You have successfully lended the book '{items}'")

        # To remove the book from the original list
        for index, keys in enumerate(list(kinglibrary.Displaybook.keys())):
            if user_lendbook_num == index:
                del kinglibrary.Displaybook[keys]

    #Method to add a book to the library
    @property
    def Addbook(self):
        print("Type the name of the book you want to add: ")
        user_addbook_bookname = input()
        user_addbook_username = input("\n Enter your name: ")
        kinglibrary.Displaybook.update({user_addbook_username.capitalize() : user_addbook_bookname.capitalize()})

        pass

    #Method to return book to the library
    def Returnbook(self):
        # input("Name the book you want to return: ")
        pass
        

# Creating an object and passing argument
kinglibrary = Library({"Shiv" : "You can win" , "Robert" : "Rich dad poor dad" , "Hari" : "Naruto Shippuden",\
    "Eichiro Oda" : "One Piece" , "Shyam" : "Pirates of the Caribbean"},"King's Library" )

while True:
    user_input = input(
        "press D to Display Book, L to Lend Book , A to Add Book and R Return Book \t")
    
    #To display books
    if user_input.upper() == "D":
        for i in enumerate(kinglibrary.Displaybook.values()):
            print(i)

    if user_input.upper() == "L":
        kinglibrary.Lendbook

    if user_input.upper() == "A":
        kinglibrary.Addbook
    
    if user_input.upper() == "R":
        break


"""     TO DO LIST:
--> Remaining to display list of books along with its owners."""