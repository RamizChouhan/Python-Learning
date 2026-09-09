#19-8-26

#variable 

name = "ramiz" #string data-type value
age=21 #integer data type value
height = 5.8 #float data type value
male = True #boolean data type value
print("------Variables------")
print("name is :",name)
print("age is :",age)
print("height is :",height)
print("male :",male)





#check type of value/ check data type
print("------Data Types------")
print(type(name),type(age),type(height),type(male)) #this all is primitive data type








#Condition Statements [if,if else, if elif, nested if else]
#if else
print("------If Eles------")
age = 17
if age > 18:
    print("eligible for vote") #block code show when codition is True
else:
    print("Not Eligible for vote")#block code show when codition is False








#if elif
print("------If Elif------")
percentage = 88
if percentage < 100 and percentage > 85:
    print("Pass Grade A")
elif percentage < 85 and percentage > 75:
    print("Pass Grade B")
elif percentage < 74 and percentage > 64:
    print("pass Grade C")
elif percentage < 63 and percentage > 45:
    print("pass grade D")
elif percentage < 44 and percentage > 35:
    print("just pass")
else:
    print("Fail")





#nested if else
print("------Nested If Else------")
num = 7
if num%2==0:
    if num%3==0:
        print ("Divisible by 2 and 3")
    else:
        print ("Divisible by 2 and not Divisible by 3")
else:
    if num%3==0:
        print("Divisible by 3 and not Divisible by 2")
    else:
        print("Not divisible by 2 and not Divisible by 3")







#Loops [for, while, do..while]
""" for loop syntax [ for variableName in sequenceData]"""
print("------For Loop------")
number = [10,20,30,40,50]
total = 0
for num in number:
    total+=num
print("total of list items:",total)



print("------While Loop------")
var = 4
while var == 4: #it execute untill condition is true
    num = int(input("choose a correct number to end this loop 1 To 10 :"))
    if num == var:
        break
    print(f"you entered : {num} !try again")
print("End Loop Good By")







print("------For Range Object------")
for i in range(5): # agar ek parameter doge to bas stop lega aur bydefault 0 se start karega
    print("for range loop i:",i)

for n in range(0,10,2):#first start,second stop,third step
    print("for range loop n:,",n)






print("------For else Loop------")
for count in range(6):
   print ("Iteration no. {}".format(count))
else:
   print ("for loop over. Now in else block")
print ("End of for loop")




#Operators [Arithmatic,Comparison,Assegnment,Logical]
""" Arithmatic operator [+,-,*,%,**,/]
    Comprison operator  [==,!=,>,<,>=,<=]
    Assegment operator  [=,+=,-=,*=,%=,**=]
    logical operator    [or,and,not] """




print("------Arithmatic Operator------")
a = 10
b = 20
#Arithmatic operator [+,-,*,%,**,/]
print("+ operator :",a+b) #30
print("- operator :",a-b) #-10
print("* operator :",a*b) #200
print("% operator :",10%2) #0 module
print("/ operator :",10/2) #5 upper value
print("** operator :",2**3) #8






#Comprison operator  [==,!=,>,<,>=,<=] it return True Or False Boolean Value
print("------Comprison Operator------")
print("== double equal to :",a==b) #false
print("!= not equal to    :",a!=b) #true
print("> greater then     :",a>b)  #false
print("< less then        :",a<b)  #true
print(">= greater then equal to :",a>=b) #false
print("<= less then equal to :",a<=b) #false






#Assegment operator  [=,+=,-=,*=,%=,**=]
print("------Assegment Operator------")
a+=a 
print("a+=a :",a)#20
a*=a
print("a*=a :",a)#100
a%=a
print("a%=a :",a)#0
b*=b
print("b*=b :",b)#400
c = 2
c**=c
print("a**=a :",c)#4
b-=b 
print("b-=b :",b)#0





