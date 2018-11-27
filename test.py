import datetime

x = int(input("Enter the age of yours"))
y = input("Enter name of yours")


now = datetime.datetime.now()

net = now.year

if x>=100:
    print("You are already a dinosaur")
else:
    er = net - x
    ter = er + 100
    (print ("Your age will be 100 years in %s" % ter))