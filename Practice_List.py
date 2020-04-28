
l=[77,55,66,55,66,55,77,44,66,55]
print(l)

#print even numbers in a list
for i in l:
    if (not(i%2)):
        print(i)


""" ""
#find smallest number in a list
#Method 1
least=0
least=l[0]
for i in l:
    if (i<least):
        least=i
#Method 2
l.sort()
print(l[0])

#Method 3
print(min(l))

print(least)
""" ""
""" ""
#Count occurrences of an element in a list
#Method 1
temp=0
for i in l:
    if(55==i):
        temp+=1
#Method 2
print(l.count(77))
print(temp)
""" ""

""" ""
#Print even numbers in a list

for i in l:
    if((i%2)==0):
        print(i)

""" ""

""" ""
#Cloning or Copying a list
#Method 1
k=l.copy()

#Method 2
k=l[0:]

#Method 3
k=list(l)



#Method 4
k=list()
for i in l:
    k.append(i)
#Method 5
k=list()
k.extend(l)

print(k)
print(id(k))
print(id(l))

""" ""


""" ""
#Finding the lement existence
#Method 1:
for i in l:
    if(i==55):
        print("Element is ptresent\n")
#Method 2:
if 55 in l:
    print("Element is presnt\n")
""" ""
""""" ""
#Finding the size of list
###### METHOD 1
l=['Sri',77,55,'sV']
print(l)
print("length of list is:",len(l))
####### METHOD 2
temp=0
for i in l:
    temp+=1
print("length of list is:",temp)
""""" ""

""" ""
#first and last elements interchange in list

l=['Sri',77,55,'sV']
print(l)
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print(l) 
""" ""
