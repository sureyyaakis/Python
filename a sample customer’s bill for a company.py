#Sureyya Betul Akis

lengthOfRoom = 0
widthOfRoom = 0
customerDiscount = 0
costPerSquare = 0  
carpet_cost = 0 
labor_cost = 0 

def main():
  acceptUserInput()
  installed_price = installedPrice(lengthOfRoom,widthOfRoom,costPerSquare)
  mainPrice(carpet_cost,labor_cost, installed_price) 
  subtotal = subTotal(installed_price, customerDiscount)
  totalPrice(subtotal)

def acceptUserInput():
  global lengthOfRoom,widthOfRoom, customerDiscount, costPerSquare
  lengthOfRoom = float(input("Enter the lenght of the room(feet)?:    "))
  widthOfRoom = float(input("Enter the width of the room(feet)?:     "))
  customerDiscount = float(input("Enter the customer discount(percent)?:  "))
  costPerSquare = float(input("Enter the cost per square foot?:        "))

def installedPrice(lengthOfRoom,widthOfRoom,costPerSquare):
  area = lengthOfRoom*widthOfRoom
  carpet_cost = area*costPerSquare
  labor_cost = area*0.35
  installed_price = carpet_cost+labor_cost
  print("")
  print("%35s" %("MEASUREMENT"))
  print("")
  print("%-16s %38d %1s" %("Lenght",lengthOfRoom,"ft"))
  print("%-16s %38d %1s" %("Width",widthOfRoom,"ft"))
  print("%-16s %38d %1s" %("Area",area,"square ft."))
  return installed_price
 
def mainPrice(carpet_cost,labor_cost, installed_price): 
  area = lengthOfRoom*widthOfRoom
  carpet_cost = area*costPerSquare
  labor_cost = area*0.35
  installed_price = carpet_cost+labor_cost
  print("")
  print("%32s" %("CHARGES"))
  print("%-20s %15s %15s" %("DESCRPTION","COST/SQ.FT.","CHARGE"))
  print("_"*55)
  print("%-20s %13.2f %12s %1.2f" %("Carpet", costPerSquare,"$",carpet_cost))
  print("%-20s %13.2f %20.2f" %("Labor", 0.35,labor_cost))
  print("%55s" %("_"*15))
  print("%-20s %26s %1.2f "%("INSTALLED PRICE","$", installed_price))
  return mainPrice
  
def subTotal(installed_price, customerDiscount):
  discount = installed_price*(customerDiscount/100)
  subtotal = installed_price-discount
  print("%-20s %13.f %1s %18.2f" %("Discount",customerDiscount,"%",discount))
  print("%55s" %("_"*15))
  print("%-19s %27s %1.2f" %("SUBTOTAL","$",subtotal ))
  return subtotal
  
def totalPrice(subtotal):
  tax = subtotal*(8.5/100)
  totalprice = subtotal+tax
  print("%-30s %24.2f" %("Tax",tax))
  print("%-30s %16s %1.2f" %("TOTAL","$",totalprice))


main()



