#lecture 4
age=input("enter age")
if int(age)>=16 and int(age)<=18:
     print("part time")
elif int(age)>18 and int(age)<65:
     print("full time")
else:
    print("not eligible")
#code2
budget=int(input("enter budget"))
if budget>=100000:
    print("asus:1 lenovo:2 other:3")
    choice=int(input("enter choice"))
    if choice == 1:
       print("bought asus")
    elif choice == 2:
        print("bought lenovo")
    else:
        print("go away >:(")
elif budget>5000 and budget<100000:
    print("lenovo:1 other:2")
    choice=int(input("enter choice"))
    if choice == 1:
        print("bought lenovo")
    else:
        print("go away")
else:
    print("i can draw a laptop or for u")

#code3
choice=input ("L,D,B");
if(choice=="B"):
    food=input("SI or NI");
    if(food=="SI"):
        c=input("idle or dosa");
        if(c=="idle"):
            print("you ordered idle");
if(choice=="L"):
    food=input("Punjabi or bihari");
    if(food=="bihari"):
        c=input("chole or littee chokha");
        if(c=="chole"):
            print("you ordered chole");
if (choice=="D"):
    food=input("maharashtrian or gujrati");
    if(food=="maharashtrian"):
        c=input("rajma chawal or biryani");
        if(c=="biryani"):
            print("you ordered biryani");
