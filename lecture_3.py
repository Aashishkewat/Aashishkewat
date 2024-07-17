
a=int(input("subject 1 "))
b=int(input("subject 2"))
c=int(input("subject 3"))
d=int(input("subject 4"))
e=int(input("subject 5"))
total_marks = a + b + c + d + e
percentage = (total_marks / 5)
print("Final percentage:", percentage)

if percentage < 35:
    print("fail")
elif percentage >= 35 and percentage < 40:
    print("passed class")
elif percentage >= 40 and percentage < 60:
    print("second class")
elif percentage >= 60 and percentage < 75:
    print("first class")
elif percentage >= 75:
    print("distinction")

