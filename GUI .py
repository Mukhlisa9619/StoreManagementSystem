from tkinter import *
import re
from tkinter import messagebox
import time
import datetime


class Staff:
    def __init__(self, name):
         self.__name = name
    @property
    def name(self): # name getter
        return self.__name
    @name.setter
    def name(self,name): # set the name
        self.__name = name

class Customer :

  def __init__(self, id):
       self.__id = id
  @property
  def id(self): # id getter
        return self.__id
  @id.setter
  def id(self,id): # set the id
        self.__id = id

class Product :
    def __init__(self, name,productCode,   price,  quantity, points,):
         self.__productCode = productCode
         self.__name = name

         self.__price = price
         self.__points = points
         self.__quantity = quantity

    def getNames(self):
        return '{} {} {} {} {}'.format(self.name, self.price, self.productCode, self.quantity, self.points)
    @property
    def productCode(self): # productCode getter
        return self.__productCode
    @productCode.setter
    def productCode(self,productCode): # set the productCode
        self.__productCode = productCode

    @property
    def name(self): # name getter
        return self.__name
    @name.setter
    def name(self,name): # set the name
        self.__name = name

    @property
    def quantity(self): # quantity getter
        return self.__quantity
    @quantity.setter
    def quantity(self,quantity): # set the quantity
        self.__quantity = quantity

    @property
    def price(self): # price getter
        return self.__price
    @price.setter
    def price(self,price): # set the price
        self.__price = price

    @property
    def points(self): # salary getter
        return self.__points
    @points.setter
    def points(self,points): # set the salary
        self.__points = points


class Order(object):
    def __init__(self,   staffObj, customerObj, quantity, productObj = []):

           self.__customerObj = customerObj
           self.__staffObj = staffObj
           self.__productObj = productObj
           self.__quantity = quantity



    @property
    def customerObj(self): # customerObj getter
        return self.__customerObj
    @customerObj.setter
    def customerObjname(self,customerObj): # set the customerObj
        self.__customerObj = customerObj

    @property
    def staffObj(self): # description getter
        return self.__staffObj
    @staffObj.setter
    def staffObj(self,staffObj): # set the staffObj
        self.__staffObj = staffObj
    @property
    def quantity(self): # quantity getter
        return self.__quantity
    @quantity.setter
    def quantity(self,quantity): # set the staffObj
        self.__quantity = quantity
    @property
    def productObj(self): # productObj getter
        return self.__productObj
    @productObj.setter
    def productObj(self,productObj): # set the staffObj
        self.__productObj = productObj


root = Tk()
root.title("Store Management System")
welcome=Label(root,text="Welcome to the Store Management System!  :)")
welcome.grid(row=0,columnspan=5,pady=20,padx=20)
welcome.grid_rowconfigure(0, weight=1)
welcome.grid_columnconfigure(0, weight=1)



name=Label(root,text="Staff Name")
id=Label(root,text="Customer ID")
labelN = Label(root)
inputName= Entry(root)
inputId=Entry(root)

name.grid(row=1, sticky=E)
labelN.grid(row=1, column=2)
inputName.focus_set()
id.grid(row=2,sticky=E)
inputName.grid(row=1,column=1)
inputId.grid(row=2,column=1)
productLabels =["Product Name","Product Code", "Price", "Quantity", "Points" ]
products =[]
row_i = 0


def addProduct():
    global row_i
    global products

    input_array = [Entry(root, width=10),
                   Entry(root, width=20),
                   Entry(root, width=6),
                   Spinbox(root, from_=1, to=100, width=5),
                   Entry(root, width=6)]
    input_array[0].grid(column=0, row=6+row_i, pady =5, padx=7)
    input_array[1].grid(column=1, row=6+row_i, pady =5, padx=7)
    input_array[2].grid(column=2, row=6+row_i, pady =5, padx=7)
    input_array[3].grid(column=3, row=6+row_i, pady =5, padx=7)
    input_array[4].grid(column=4, row=6+row_i, pady =5, padx=7)



    products.append(input_array)
    row_i+=1

regex=re.compile(r'[a-zA-Z]', flags=re.IGNORECASE)
regex2=re.compile(r'\d', flags=re.IGNORECASE)

def printF():

    p_list = []
    sum = 0;
    for row in products:
     if regex.match(row[0].get()) and regex2.match(row[2].get()) and regex2.match(row[4].get()):

       p_list.append(Product(row[0].get(), row[1].get(), row[2].get(),  row[3].get(), row[4].get()))

     else:
        messagebox.showwarning("Regular Expression", "Please verify whether Product name is a STRING and price and points are INTEGER!")


    window = Toplevel(root)

    window.title("Store Management System")
    welcome=Label(window,text="Welcome to the Store Management System!  :)")
    welcome.grid(row=0,columnspan=5,pady=20,padx=20)
    welcome.grid_rowconfigure(0, weight=1)
    welcome.grid_columnconfigure(0, weight=1)

    if regex.match(inputName.get()):
        nameStaff = Staff(inputName.get())

    else:
        messagebox.showwarning("Regular Expression", "Staff name must be string!")


    idCustomer = Customer(inputId.get())
    o = Order(nameStaff, idCustomer, sum, p_list)
    name=Label(window,text="Staff Name")
    id=Label(window,text="Customer ID")
    outputName= Label(window,text="name")
    outputId=Label(window,text="id")

    name.grid(row=1, sticky=W)
    Label(window,text=o.staffObj.name).grid(row=1 ,column=1)
    id.grid(row=2,sticky=W,pady=(5,10))

    Label(window,text=o.customerObj.id).grid(row=2,column=1,pady=(5,10))
    labelN = Label(window)
    labelN.grid(row=1, column=2)




    #stringD = "name:"+ nameStaff.name + idCustomer.id

    pName=Label(window,text="Product Name")
    pCode=Label(window,text="Product Code")
    pPrice=Label(window,text="Price")
    pQuantity=Label(window,text="Quantity")
    pPoints=Label(window,text="Points")
    pName.grid(row=5,column=0,  padx=30)
    pCode.grid(row=5,column=1, padx=30)
    pPrice.grid(row=5,column=2, padx=30)
    pQuantity.grid(row=5,column=3, padx=30)
    pPoints.grid(row=5,column=4,padx=30)
    row = 6
    sum=0
    totalPrice = 0
    totalPoints = 0
    def close():
       window.destroy()

    for (index, item) in enumerate(o.productObj):


        Label(window,text=item.name).grid(row=row + index, column=0)
        Label(window,text=item.productCode).grid(row=row + index, column=1)
        Label(window,text=item.price).grid(row=row + index, column=2)
        Label(window,text=item.quantity).grid(row=row + index, column=3)
        sum = sum+int(item.quantity)
        totalPrice = totalPrice+int(item.price)*int(item.quantity)

        Label(window,text=item. points).grid(row=row + index, column=4)
        totalPoints = totalPoints + int(item.points)
    Label(window,text="Total Items:  " +str(sum)).grid(row=45, column=0, sticky=W,pady=(20,0))
    Label(window,text="Total Price:  " +str(totalPrice)).grid(row=46, column=0, sticky=W)
    Label(window,text="Points:       " +str(totalPoints)).grid(row=47, column=0, sticky=W)
    Button(window,text="Close",command=close).grid(row=58,column=4,sticky=E,pady=20,padx=20)







add=Label(root, text="Add more products")
addButton=Button(root,text="+",command=addProduct)



add.grid(row=4,column=0,pady=30, padx=30)
addButton.grid(row=4, column=0,sticky=E)


def close():
    root.destroy()

print=Button(root,text="Print",command=printF)
close=Button(root,text="Close",command=close)
print.grid(row=45+row_i,column=0,pady=20,sticky=E)
close.grid(row=45+row_i,column=1,columnspan=2,pady=20)

pName=Label(root,text="Product Name")
pCode=Label(root,text="Product Code")
pPrice=Label(root,text="Price")
pQuantity=Label(root,text="Quantity")
pPoints=Label(root,text="Points")
pName.grid(row=5,column=0)
pCode.grid(row=5,column=1)
pPrice.grid(row=5,column=2, padx=30)
pQuantity.grid(row=5,column=3, padx=30)
pPoints.grid(row=5,column=4,padx=30)
addProduct()
#addF(5,6,10)

root.mainloop()