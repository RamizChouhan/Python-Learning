"""name="ramiz"
age=21
height=5.8
is_student=True

print("name is :",name)
print("age is :",age)
print("height is :",height)
print("student :",is_student)

print("data type for name :",type(name))
print("data type for age :",type(age))
print("data type for height :",type(height))
print("data type for is_student :",type(is_student))"""

'''num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))

print("Addition OF Two Number Is :",num1+num2)
print("Subtration OF Two Number Is :",num1-num2)
print("Multipication OF Two Number Is :",num1*num2)
print("Division OF Two Number Is :",num1/num2)
print("Modulus OF Two Number Is :",num1%num2)'''

'''num=int(input("Enter A Number For Checking Even or Odd :"))
if num%2==0:
    print(f"{num} Number Is A Even Number")
else:
     print(f"{num} Number Is A Odd Number")'''

'''num=int(input("enter a number for checking positive or negative :"))

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print("number is zero ")'''

'''num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
num3=int(input("Enter Third Number :"))

if num1 >= num2 and num1 >= num3:
    print(f"First number {num1} is Greater Then number:{num2} or number:{num3}")
elif num2 >= num1 and num2 >= num3:
    print(f"Second number {num2} is Greater Then number:{num1} or number:{num3}")
else:
    print(f"third number {num3} is Greater Then number:{num1} or number:{num2}")'''


'''num=int(input("Enter Number For Table :"))
result=0
for i in range(1,11):
    result = num*i
    print(f"{num}x{i}={result}")'''

'''num=int(input("enter a number for calculate sum :"))
result = num*num
print(result)'''


'''num=int(input("Enter A Number :"))

for i in range(1,num+1):
    if i%2==0:
        print(i)'''

num=int(input("Enter A Number :"))
if num > 0:
    print("number is positive")
    if num%2==0:
        print("number is even")
        for i in range(1,num+1):
            print(i)
    else:
        print("number is odd")
        for i in range(1,num+1):
            print(i)
elif num == 0:
              print("number is zero")
else:
    print("number is negative")

