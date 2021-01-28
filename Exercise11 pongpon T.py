numberinput = int(input("ใส่จำนวนรอบ: "))
n1 = numberinput
#n2 = numberinput
for x in range(numberinput):
    n1 -= 1
    #n2 -= 2
    print(" "*n1,"*"*(x*2+1))