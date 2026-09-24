#A set is an unordered, mutable collection of unique elements in Python.
#Set is generally written using curly braces {}.

st = {2,4,5,6,8,2,9,22}
print(st)#print

#built in methods
print("-----Set Methods------")
st.add(3) #add element

st.update(["a","B","c"]) #update set 

st.remove(22) #remove elements if nhi mila to error dega

st.discard(2)#remove elements if nhi mila to error nhi dega

x= st.pop()
print("pop element :",x)

print("-----Math Methods-----")
a = {2,4,6,1,3}
b = {1,3,5,4}
print("all elements :",a.union(b))
print("commom elememts :",a.intersection(b))
print("different elements :",a.difference(b))#Jo elements first set mein hain but second mein nahi.
print("symmetic difference :",a.symmetric_difference(b))#Jo elements sirf ek set mein hain, common elements nahi.


#Update version Ye methods original set ko modify karte hain.
print("-----Update version-----")
a.intersection_update(b)
print(a)

a.difference_update(b)
print(a)


a.symmetric_difference_update(b)
print(a)


#. Checking / Relationship Methods
print("-----Checking / Relationship Methods-----")
x = {1,3}
y = {0,1,2,3,4,7,8}
print(x.isdisjoint(y))#Check karta hai ki dono sets mein koi common element hai ya nahi.

print(x.issubset(y))#Check karta hai ki first set, second set ka subset hai ya nahi.
print(y.issuperset(x))#Check karta hai ki first set mein second set ke saare elements hain ya nahi.

#set functions
print("-----set functions-----")
s = {10, 20, 30}

print(len(s))       # 3
print(max(s))       # 30
print(min(s))       # 10
print(sum(s))       # 60
print(sorted(s))    # [10, 20, 30]
