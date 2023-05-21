#Lists
mangaCode=[122020,162019,242020]
mangaCategory=["Manwha","Manga","Manga"]
mangaTittle=["Solo Leveling","Tomochan wa Onnanoko","Onepunch Man"]
mangaPrice=[23,25,18]
mangaQuantity=[12,17,20]
#Function1
def Add_Code():
    bookCode=int(input("Enter book code "))
    while bookCode in mangaCode:
        bookCode=int(input("Book code already registered, enter a new code: "))
    mangaCode.append(bookCode)
    bookCategory=input("Enter book category ")
    mangaCategory.append(bookCategory)
    bookTittle=input("Enter tittle")
    mangaTittle.append(bookTittle)
    bookPrice=float(input("Enter price"))
    mangaPrice.append(bookPrice)
    print("Please enter quantity between 10 and 50")
    bookQuantity=int(input("Enter Quantity"))
    while bookQuantity not in range(10,51):
        bookQuantity=int(input("Enter a valid Quantity"))
    mangaQuantity.append(bookQuantity)
    return mangaCode, mangaCategory, mangaTittle, mangaPrice, mangaQuantity
#Function2
def Check_Product():
    bookCode=int(input("Enter book Code"))
    if bookCode in mangaCode:
        print("That book code is already registered")
    else:
        print("That book code is not yet registered")
#Function3
def Search_Product():
    global bookPosition
    bookPosition=0
    bookCode=int(input("Please Enter book code: "))
    while bookCode not in mangaCode:
        bookCode=int(input("Enter a valid code: "))
    else:
        for i, j in enumerate(mangaCode):
            if j == bookCode:
                bookPosition=i
                print("Book Detail")
                print("Category:",mangaCategory[i])
                print("Tittle:",mangaTittle[i])
                print("Price:",mangaPrice[i])
                print("Quantity:",mangaQuantity[i])
#Function4
def Update_Product():
    Search_Product()
    updateCategory=input("Do you want to update book category, yes or no?: ")
    while updateCategory != "go":
        if updateCategory == "yes":
            newCategory=input("Please enter new Category: ")
            mangaCategory[bookPosition]=(newCategory)
            updateCategory="go"
        elif updateCategory =="no":
            updateCategory="go"
        else:
            updateCategory=input("Do you want to update book category, yes or no?: ")
    updateTittle=input("Do you want to update book tittle, yes or no?: ")
    while updateTittle != "go":
        if updateTittle == "yes":
            newTittle=input("Please enter new Tittle: ")
            mangaTittle[bookPosition]=(newTittle)
            updateTittle == "go"
        elif updateTittle == "no":
            updateTittle = "go"
        else:
            updateTittle=input("Do you want to update book tittle, yes or no?: ")
    updatePrice=input("Do you want to update book price, yes or no?: ")
    while updatePrice != "go":
        if updatePrice == "yes":
            newPrice=float(input("Please enter new Price: "))
            mangaPrice[bookPosition]=(newPrice)
            updatePrice = "go"
        elif updatePrice == "no":
            updatePrice = "go"
        else:
            updatePrice=input("Do you want to update book price, yes or no?: ")
    updateQuantity=input("Do you want to update book quantity, yes or no?: ")
    while updateQuantity != "go":
        if updateQuantity == "yes":
            newQuantity=int(input("Please enter new Quantity: "))
            while newQuantity not in range(10,51):
                newQuantity=int(input("Enter a valid Quantity: "))
                mangaQuantity[bookPosition]=(newQuantity)
                updateQuantity = "go"
        elif updateQuantity == "no":
            updateQuantity="go"
        else:
            updateQuantity=input("Do you want to update book quantity, yes or no?: ")     
    return mangaCategory, mangaTittle, mangaPrice, mangaQuantity
#Funtion5
def Buy_Product():
    productCode=int(input("Please enter the code of the book you want to buy: "))
    while productCode not in mangaCode:
        productCode=int(input("Please enter a valid code of the book you want to buy: "))
    else:
        for i, j in enumerate(mangaCode):
                if j == productCode:
                    productQuantity=int(input("please enter product quantity"))
                    while productQuantity > mangaQuantity[i]:
                        print("There are", mangaQuantity[i],"quantities of the book '", mangaTittle[i], "' available for sale")
                        answer=input("Do you want to enter new quantity? Enter yes or no: ")
                        if answer == "yes":
                            productQuantity=int(input("please enter product quantity: "))
                        elif answer == "no":
                            productQuantity=0
                    leftBooks=mangaQuantity[i]-productQuantity
                    mangaQuantity[i]=(leftBooks)
                    bookSave=0
                    if productQuantity in range(10,20):
                        bookSave=0.10
                    elif productQuantity in range(20,30):
                        bookSave=0.20
                    elif productQuantity in range(30,51):
                        bookSave=0.30
                    productCost=(productQuantity*mangaPrice[i]-((productQuantity*mangaPrice[i])*bookSave))+(productQuantity*mangaPrice[i])*0.15
                    print("The total price to pay is $", round(productCost,1))
        return mangaQuantity
#main program
print("Please select one of the following options")
print("1. Add Product")
print("2. Check Product")
print("3. Search Product")
print("4. Update Product")
print("5. Buy Product")
print("6. Exit")   
command=input("Please enter 1, 2, 3, 4, 5 or 6: ")
while command != "6":
    if command == "1":
        Add_Code()
        answer=input("Do you want to add another book, yes or no: ")
        while answer == "yes":
            Add_Code()
            answer=input("Do you want to add another book, yes or no")
    elif command == "2":
        Check_Product()
    elif command =="3":
        Search_Product()
    elif command =="4":
        Update_Product()
    elif command =="5":
        Buy_Product() 
    input("Press enter to continue")
    print("Please select one of the following options")
    print("1. Add Product")
    print("2. Check Product")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Buy Product")
    print("6. Exit")   
    command=input("Please enter 1, 2, 3, 4, 5 or 6: ")
