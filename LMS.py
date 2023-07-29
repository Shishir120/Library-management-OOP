#Currently working here...... 12/15/2022   4:34 PM "Main program committed"

import time

class Library:


    def __init__(self, listofbooks, library_name) -> None:
        self.listofbooks = listofbooks
        self.library_name = library_name
        self.lenddict = {}
        self.adddict = {}
        self.returndict = {}

    #To create the file and take log   (Working fine) 12/15/2022
    def lend_logs(self, lenddict):
        t = time.asctime()
        with open("User_logs.txt" , "a") as f:
            f.write(f"{lenddict} taken on {t} \n")

    def add_logs(self, adddict):
        t = time.asctime()
        with open("Book_Add_logs.txt" , "a") as f:
            f.write(f"Added {adddict} on {t} \n")

    def return_logs(self , returndict):
        t = time.asctime()
        with open ("Return_logs.txt" , "a") as f:
            f.write(f"Returned {returndict} on {t} \n")

        pass 

    @property
    def Displaybook(self):
        # To display the available books
        return self.listofbooks


    #Method to lend books
    @property
    def Lendbook(self):
        print("Which book do you want to lend?")
        for i in enumerate(kinglibrary.listofbooks):   #To display index along with books.
            print(i)
        
        user_lendbook_username = input("Enter your name: ")
        user_lendbook_num = int(input("Select a book number:  "))
        for index, items in enumerate(kinglibrary.listofbooks): 
            if user_lendbook_num == index:
                print(f"You have successfully lended the book '{items}'")
                self.lenddict = {user_lendbook_username : items}         #Creating a dictionary about user who took the book
                
                kinglibrary.lend_logs(self.lenddict)            #Calling user-defined function
            
                #To remove the book from the original list
                kinglibrary.listofbooks.remove(items)    #In-built function


    #Method to add a book to the library
    @property
    def Addbook(self):
        print("Type the name of the book you want to add: ")
        user_addbook_bookname = input()
        user_addbook_username = input("\n Enter your name: ")
        kinglibrary.adddict.update({user_addbook_username.capitalize() : user_addbook_bookname.capitalize()})
        kinglibrary.listofbooks.append(user_addbook_bookname.upper())

        var1.append(user_addbook_bookname.upper())

        self.adddict = {user_addbook_username : user_addbook_bookname}
        kinglibrary.add_logs(self.adddict)      #User-Defined function

        pass


    #Method to return book to the library
    @property
    def Returnbook(self):
        user_return_name = input("Enter your name: ")
        user_returnbook_bookname = input("Name the book you want to return: ")

        for items in var1:          #Using copy of list i.e var1.
            if user_returnbook_bookname.upper() == items:
                kinglibrary.listofbooks.append(user_returnbook_bookname.upper())
                self.returndict = {user_return_name: user_returnbook_bookname}
                kinglibrary.return_logs(self.returndict)
                break

        

# Creating an object and passing argument
kinglibrary = Library(["YOU CAN WIN" ,"RICH DAD POOR DAD" ,"NARUTO SHIPPUDEN",\
    "ONE PIECE","PIRATES OF THE CARIBBEAN"],"King's Library" )

var1 = kinglibrary.Displaybook.copy()        # Idea For making copy of books available in the library

print("\n \t \t Welcome To The Library Management System: \n")

#Start of infinite loop
while True:

    user_input = input("Press D to Display Available Books, L to Lend Book , A to Add Book , R to Return\
 Book and E to exit the Library: ")
    
    #To display books
    if user_input.upper() == "D":
        for i in enumerate(kinglibrary.Displaybook):
            print(i)

    elif user_input.upper() == "L":       #To lend Books
        kinglibrary.Lendbook

    elif user_input.upper() == "A":       #To Add Books
        kinglibrary.Addbook
        
    elif user_input.upper() == "R":       #To Return Books
        kinglibrary.Returnbook
        
    elif user_input.upper() == "E":
        break
        
    else:
        print("Wrong Input...")


"""     TO DO LIST:
--> Remaining to display list of books along with its owners."""