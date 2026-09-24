#A dictionary is an ordered, mutable collection of key-value pairs in Python.
#It is written using curly braces {}.

student = {
    "name":"ramiz",
    "age":20,
    "subject":["Os","CSA","Py","DBMS"],
    "marks":59.32,
    "male":True,
 }

print(student) # whole student info

print("Subjects :",student.get("subject")) #specifice values

print("all keys :",student.keys())#print all keys

print("all values :",student.values()) #print all values

'''print("seperate key and values :",student.items())

for key,value in student.items():
    print(key,":",value)'''

student.update({"age": 22, "course": "BCA"})
print(student)

x=student.pop("course")
print(student)

x = student.popitem()

print(x)
print(student)


keys = ["name", "age", "course"]

st = dict.fromkeys(keys, "Not Available")
#Given keys se new dictionary create karta hai, aur sabhi keys ko same value de sakte ho.
print(st)


student.setdefault("course", "BCA")

print(student)

    
