
#31-8-26

#creating list

mylist = [10,"A",True,42.52] #square bracket
#print(mylist) #[10, 'A', True, 42.52]

a = list("ramiz")#list constructor
#print(a) #['r', 'a', 'm', 'i', 'z']

num = [2] * 10 # repeatation
#print(num) #[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

#accessing list elements
#print(mylist[1]) # A

#method add element in existing list
mylist.append("SE") #last index per add 
#print(mylist) # [10, 'A', True, 42.52, 'SE']

mylist.insert(0,"karan") #specifi index add elements
#print(mylist) #['karan', 10, 'A', True, 42.52, 'SE']

marks = [53,51,34,62] #add a new list in a existing list
mylist.extend(marks)
#print(mylist) #['karan', 10, 'A', True, 42.52, 'SE', 53, 51, 34, 62]


mylist[2] = "B" #updating existing list 
# print(mylist)

num = [1,2,3,4,2,5]
num.remove(2) #remove method
print(num)
num.pop(3) # remove items from last index or specific index
print(num)


num2 = [2,5,6,7,5,9,5] 
del num2[5] # delete item from specific index
print(num2)

num2.clear() # empty list output
print(num2)


alphabets = ["a","b","c","d","e"]
print(alphabets)

for al in alphabets:
    print(al)


a = [[1, 2], [3, 4]] #nested list 
print(a[0])
print(a[1][0])



