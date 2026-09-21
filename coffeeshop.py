#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")


#Koden spør deg om hvilken type kaffe du har lsyt å tar prisen av kaffen får deg.
price = 0
coffee = input("What type of coffee would you like? ").title()
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3.00
elif coffee=="Latte":
   price = price + 2.50
elif coffee=="Cappuccino":
   price = price + 3.00
elif coffee=="Macchiato":
   price = price + 2.50
elif coffee=="Mocha":
   price = price + 3.50
elif coffee=="Flat White":
   price = price + 2.50

#Koden sprø deg om hva type strørrelse du har lyst på
size = input("Do you want Medium, Large, Extra Large ").title()
if size=="Medium":
   price = price + 0
elif size=="Large":
   price = price + 1.00
elif size=="Extra Large":
   price = price + 1.50

#Denne koden spør deg om du vil ea in eller ta take away
eatin = input("Do you want to eat in or take away? ").title()
if eatin=="Eat In":
   price = price + 0
elif eatin=="Take Away":
   price = price + 1.00


#Complete the code here...
print("----------------------------")
print("Total Cost: £" + str(price))