pricelist =[]
menuList = []
def showbill():
    priceTotal=0
    print("___________My Food Bill___________")
    for number in range(len(menuList)):
        print(menuList[number],pricelist[number])
        priceTotal += int(pricelist[number])
    print("total bill is $",priceTotal)
while True:
    menuName = input("Please enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        pricelist.append(menuPrice)
showbill()