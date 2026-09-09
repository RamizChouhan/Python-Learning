#9-9-26

#A tuple is an ordered, immutable collection of elements
#that can contain duplicate and different types of values.
tple = (21,56.4,24,74,32,5,43,5,2,64,86,5,74,44,5) # creation tuple

print("tuple :",tple) # complete tuple print
print("specific value :",tple[0],tple[2]) # specific value using index

'''for val in tple:
    print(val)'''  #print value one by one

#tuple built in methods and tuple have only 2 methods index/count
print("------tuple methods----------")
print("value 2 index",tple.index(2)) # print element index

print("count 5 :",tple.count(5)) #Kisi element ki occurrence count karta hai.

#tuple built in functions
print("------tuple Functions----------")
print("tuple length :",len(tple))

print("tuple maximum :",max(tple))

print("tuple minimum :",min(tple))

print("tuple sorted :",sorted(tple))


tple2 = (0,0,0,1,0,0)
print("tuple any :",any(tple2))
print("tuple all :",all(tple2))


