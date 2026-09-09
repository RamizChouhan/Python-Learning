#21-8-26

"""a = 100
b = 20.5
c = a+b #implicit
print(type(c)) #float because python data lose nhi karta float ke point ka
num1 = "20"
print(type(num1))
num = int("10") #explicit
print(type(num))"""


#function argument default
'''def sum(x,y=10):
    return x+y

total = sum(10,30)
print(total)'''

#keyword argument
'''def student(name,age):
    print("i am :",name)
    print("my age is :",age)

student(age=21,name="ramiz")'''
#Positional Argument
#student("ramiz",21)


#Arbitrary Arguments handle multiple arguments
'''def num(*n,**keyvlaue):#tuple datatype
    for key,value in keyvlaue.items():
        print(f"{key}==={value}")
    print(type(n))
    for i in n:
        print(i)#int datatype

num(3,234,55,9,7,5,6,"r","a","m","i","z",name="ramiz",age=21)'''



