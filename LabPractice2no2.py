import random

choice = int(input("Select 1 for ascending or 2 for descending: "))

if choice==1:
 number1 = random.randint(1,100)
 number2 = random.randint(1,100)
 number3 = random.randint(1,100)
 number4 = random.randint(1,100)
 number5 = random.randint(1,100)
 a = sorted([number1,number2,number3,number4,number5])
 print a
elif choice==2:
 number1 = random.randint(1,100)
 number2 = random.randint(1,100)
 number3 = random.randint(1,100)
 number4 = random.randint(1,100)
 number5 = random.randint(1,100)
 b = sorted([number1,number2,number3,number4,number5],reverse=True)
 print b
else:
 print "Wrong choice"
print "Done"
