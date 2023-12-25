print("***********welcome to  drinks stall Online***********")
Username = input("Enter your Username :")
Password = input("Enter your Password :")
if Username == "TaeNannapat" or Password == "4848":
    print("***********Please select the desired item.***********")
    print("1.","Drink Water","15","THB")
    print("2.","Iced Cocoa","30","THB")
    print("3.","Iced tea", "25", "THB")
    print("4.","lemon tea", "25", "THB")
    print("What do you want to buy?")
    water = int(input("ใส่ตัวเลขสินค้า:        "))
    if water == 1 :
        amout1 = int(input("ต้องการจำนวนเท่าไหร่:"))
        total = amout1*15
        print("***********")
        print("total",total,"THB")
        print("******Thank you*****")
    elif water == 2 :
        amout1 = int(input("ต้องการจำนวนเท่าไหร่:"))
        total = amout1*30
        print("***********")
        print("total",total,"THB")
        print("******Thank you*****")
    elif water == 3 :
        amout1 = int(input("ต้องการจำนวนเท่าไหร่:"))
        total = amout1*25
        print("***********")
        print("total",total,"THB")
        print("******Thank you*****")
    elif water == 4 :
        amout1 = int(input("ต้องการจำนวนเท่าไหร่:"))
        total = amout1*25
        print("***********")
        print("total",total,"THB")
        print("******Thank you*****")
else :
    print("error")