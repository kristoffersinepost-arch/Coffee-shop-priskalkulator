
# 1. Datastrukturer (Ordbøker / Dictionaries for priser)
coffee_meny = {
   "Espresso": 2.50,
   "Americano": 3.00,
   "Latte": 2.50,
   "Cappuccino": 3.00,
   "Macchiato": 2.50,
   "Mocha": 3.50,
   "Flat White": 2.50
}

size = {
   "Medium": 0,
   "Large": 1.00,
   "Extra Large": 1.50
}

eatin_valg = {
   "Eat In": 0,
   "Take Away": 1.00
   
}

#Funksjon for å hente og validere brukerens input
def validering_ombruker(sporsmal, meny):
    """
    Spør brukeren helt til de oppgir et valg som finnes i menyen.
    Returnerer det gyldige valget.
    """
    while True:
        svar = input(sporsmal).title().strip() 
        if svar in meny:
            return svar
        print(f"ikke et gyldig valg '{svar}'. Prøv med et annet alternativ fra listen.\n")

#Denne koden skirve ut menyen for oss
def vis_meny(tittel, meny):
    print("----------------------------")
    print(tittel)
    for valg in meny:
        print(f" > {valg}")
    print("----------------------------")    


#Her begynner hovedprogrammet i koden

def hoverporgrammet():
   print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
   print("+                               +")
   print("+         The Coffee Shop       +")
   print("+              Welcome          +")
   print("+                               +")
   print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

   total_pris = 0.0 

   #Du velger kaffe her 
   vis_meny("We serve these following coffee", coffee_meny)
   valgt_coffee = validering_ombruker("What type of coffee  you like? ", coffee_meny)
   total_pris += coffee_meny[valgt_coffee]

   #Du velger hva type størrelse du vil ha
   vis_meny("We have these following sizes for your coffee", size)
   valgt_size = validering_ombruker("what size do you want ", size)
   total_pris += size[valgt_size]

   #Her velger du om du vil ta take away eller eat in
   vis_meny("Do you want take away or eat in", eatin_valg)
   valgt_eatin = validering_ombruker("Chochoose one of them", eatin_valg)
   total_pris += eatin_valg[valgt_eatin]

   #skirver ut en oppsumering av bestillingen din
   print("----------------------------")
   print("Order summry")
   print(f" - Coffee: {valgt_coffee} ")
   print(f" - Size: {valgt_size} ")
   print(f" - Serving: {valgt_eatin}")
   print("----------------------------")
   print(f" Total cost: {total_pris} ")

hoverporgrammet()