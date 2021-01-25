Usernameinput = input("Username :")
Passwordinout = input("Password :")
if Usernameinput == "admin" and Passwordinout == "1234":
    a = 10
    b = 20
    c = 7500
    d = 2750
    print("1.apple :", a)
    print("2.banana :", b)
    print("3.cat :",c)
    print("4.dog :",d)
    userSelected = int(input("เลือกสินค้า :"))
    totel =0
    if userSelected == 1:
        totel = int(input("ใสจำนวนที่จะซื้อ :"))
        print("Total =", totel*a)
        print("ขอบคุณครับ")
    elif userSelected ==2:
        totel =int(input("ใส่จำนวนที่จะซื้อ :"))
        print("Total =", totel*b)
    elif userSelected ==3:
        totel =int(input("ใส่จำนวนที่จะซื้อ :"))
        print("Total =", totel*c)
    elif userSelected ==4:
        totel =int(input("ใส่จำนวนที่จะซื้อ :"))
        print("Total =", totel*d)
    else:
        print("รหัสผ่านไม่ถูกต้อง")