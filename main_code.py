# GUI for Library

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile

root = Tk()
root.title('LIBRARY GUI')
root.geometry("1250x640")
root.configure(bg='black')

bn = []
bid = []
bc = []
newbooklist = []
name = " "
cost = 0
id = 0


def reversecontents():
    bn.reverse()
    messagebox.showinfo('RESULT',bn)


def add():
    main_name = name.get()
    bn.append(main_name)
    main_ids = ids.get()
    bid.append(main_ids)
    int_cost = int(cost.get())   #important string to int conversion
    bc.append(int_cost)


#def addbooks():
    #print("You need to add the books to the library first")
    #n = int(input("enter the number of books you wanna add"))
#    for i in range(0, int(n)):
        #name = input("Enter the name of the book :")
#        bn.append(name)
        #ids = input("Enter the id of the book  :")
#        bid.append(ids)
        #cost = int(input("Enter the cost of the book :"))
#        bc.append(int(cost))


#print(addbooks())


def addmorebooks():
    print("Okay!!,You wanna add more")
    w = int(input("enter the number of books you wanna add"))
    for i in range(0, w):
        name = input("Enter the name of the book :")
        bn.append(name)
        ids = input("Enter the id of the book :")
        bid.append(ids)
        cost = input("Enter the cost of the book :")
        bc.append(cost)


def arrangebooks():  # bubble sort         works
    for i in range(0, len(bn) - 1):
        for j in range(i):
            if bn[j + 1] < bn[j]:
                c = bn[j]
                bn[j] = bn[j + 1]
                bn[j + 1] = c    #print(bn)
        messagebox.showinfo('RESULT',bn)
        #listbox = Listbox(root)
        #listbox.insert(0,bn)
        #listbox.pack()


def countbooks():          # works
    count = 0
    for cost in bc:
        if (cost > 500):
            count += 1
    messagebox.showinfo('RESULT',f"The number of books whose cost is more than 500 = {count}")


def copybooks():
    new = []
    for i in bn:
        if i not in new:
            new.append(i)
    messagebox.showinfo('RESULT',f"The updated list without duplicates using a temporary array is = {new}")


def deleteduplicate():
    for cost in bc:
        if cost < 500:
            newbooklist.append(name)

    messagebox.showinfo('RESULT',f"The updated list of books are = {newbooklist}")


def full_reset():
    name.delete(0, END)
    ids.delete(0, END)
    cost.delete(0, END)


#def menu():
    # Menu print
#    print("Choose the operation you want to perform")
#    print("1: Add more books to the Library")   #Add new button added
#    print("2: Display books in ascending order on the basis of cost")   #msgbox
#    print("3:Delete duplicate entries using a temporary array")     #msgbox
#    print("4:Count the number of books which cost more than 500")  #msgbox
#    print("5:Copy books in a new list which have cost less than 500")    #msgbox
#    print("6:Reverse contents of the library books")   #msgbox
#    print("Thanks for the mess!")
#    choice = int(input("Enter your choice!"))
#    while choice != 0:
#        if choice == 1:
#            addmorebooks()
#            break
#        elif choice == 2:
#            arrangebooks()
#            break
#        elif choice == 3:
#            deleteduplicate()
#            break
#        elif choice == 4:
#            countbooks()
#            break
#        elif choice == 5:
#           copybooks()
#            break
#        elif choice == 6:
#            reversecontents()
#            break
#        else:
#           break


# GUI code --------------------------------------------------------



#main()
#Labels------------------------------

mylabel1 = Label(root, text='GUI for Library App', font=("Arial Bold", 20, 'underline') , fg='cyan', bg='black')
mylabel1.pack()

#mylabel2 = Label(root, text='Enter the Number of Books you want to Add :', font=('Arial', 15), bg='black', fg='white')
#mylabel2.place(x=135, y=55)

mylabel3 = Label(root, text='Enter the Name of the Book :', font=('Arial', 15), bg='black', fg='white')
mylabel3.place(x=135, y=90)

mylabel4 = Label(root, text='Enter ID of the Book :', font=('Arial', 15), bg='black', fg='white')
mylabel4.place(x=135, y=125)

mylabel5 = Label(root, text='Enter Cost of the Book :', font=('Arial', 15), bg='black', fg='white')
mylabel5.place(x=135, y=160)

#Buttons------------------------------

Add_book = Button(root, text='ADD BOOK', fg='white', bg='red', width=20,height=6, font='sans 10 bold', command=add).place(x=600, y=85)
Arrange_books = Button(root, text='ARRANGE BOOK IN ASCENDING ORDER ON COST', fg='white', bg='red', width=55,height=2, font='sans 10 bold', command=arrangebooks).place(x=135, y=345)
Delete = Button(root, text='DELETE DUPLICATE ENTRIES', fg='white', bg='red', width=55,height=2, font='sans 10 bold', command=deleteduplicate).place(x=135, y=255)
Count = Button(root, text='NUMBER OF BOOKS EXPENSIVE THAN 500', fg='white', bg='red', width=55,height=2, font='sans 10 bold', command=countbooks).place(x=135, y=300)
Copy = Button(root, text='COPY BOOKS IN A NEW LIST WHICH HAS COST LESS THAN 500', fg='white', bg='red', width=55,height=2, font='sans 10 bold', command=copybooks).place(x=135, y=435)
Reverse = Button(root, text='REVERSE CONTENT OF THE LIBRARY BOOKS', fg='white', bg='red', width=55,height=2, font='sans 10 bold', command=reversecontents).place(x=135, y=390)
Add_new_book = Button(root, text='ADD NEW BOOK', fg='white', bg='red', width=55,height=2, font='sans 10 bold', command=full_reset).place(x=135, y=210)

#Entry--------------------------------

#n = Entry(root, bg='misty rose', fg='black')
#n.place(x=540, y=55, width=50, height=27)

name = Entry(root, bg='misty rose', fg='black')
name.place(x=400, y=90, width=190, height=27)

ids = Entry(root, bg='misty rose', fg='black')
ids.place(x=400, y=125, width=190, height=27)

cost = Entry(root, bg='misty rose', fg='black')
cost.place(x=400, y=160, width=190, height=27)

root.mainloop()
