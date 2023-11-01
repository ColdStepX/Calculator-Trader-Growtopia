#Menu Select
print("")
print("======== CALCULATOR TRADE GROWTOPIA ========")
print("This calculator will help you to accounting items or seeds especially for Mass \n\tby ColdStepX")
print("")
print("======== How to select? ========" )
print("Just type the number to select :D" )
print("")
print("======== Select Calculator ========" )
print("Calculator Type: \n\t1. Vend Price \n\t2. Trader Price" )
calculatortype = (input("Select your calculator type: "))


if calculatortype == "1" :
    #Input Vend Price
    print("")
    print("======== Calculator Vend Price ========" )
    totalitem = float(input("How many item you need? = "))
    itemrate = float(input("How much rate price ?/wl: ")) 

    #Calculating
    pricetotalitem = totalitem / itemrate

    #Output
    print("==== OUTPUT ====")
    print("The World Lock you need for",pricetotalitem,"World Lock")




elif calculatortype == "2" :
    #Input Trader Price
    print("")
    print("======== Calculator Trader Price ========" )
    print(" Hint:\n\tSeller: Sell 5 dirt per 3 world lock \n\t(sell 5 dirt) = rate item \n\t(per 3 world lock) = wl per item")
    print("")
    totalitem = float(input("How much item you need?: "))
    itemrate = float(input("How much rate item?: "))
    itemwlrate = float(input("How much wl per item?: "))  

    #Calculating
    pricetotalitem = (itemwlrate * totalitem) / itemrate
     
    #Output
    print("")
    print("======== OUTPUT ========")
    print("The World Lock you need for: ",pricetotalitem,"World Lock")
    print("")
else: print("Calculator Unavailable")


