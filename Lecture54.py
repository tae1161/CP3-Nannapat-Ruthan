def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "1234":
        return showMenu()
    else:
        print("password eorro")
        return login()
def showMenu():
    print("--------shop--------")
    print("1. Vat Calcurator")
    print("2. Price Caculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input("Enter your choice: "))
    if userSelected == 1:
        return vatCaculate(totalprice=int(input("Product Price")))
    elif userSelected == 2:
        return priceCalcuatr()
    else:
        print("Invalid")
        return menuSelect()
def vatCaculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat/100)
    return  result
def  priceCalcuatr():
    price1 = int(input("Frist Product Price :"))
    price2 = int(input("Second Product PRICE :"))
    return vatCaculate(price1+price2)

print(login())