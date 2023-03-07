#List 21: 
My_list=[1,2,3,4,5,6,7]
print(My_list[0])
print(My_list[-1])
My_list[0]=3
print(My_list)
#list metodes: 

#appends methode to adedd items to the list from the end
mylist2=["nmaa","osama","hamza","Laith"]
mylist2.append("anas")
mylist2.append(100)
mylist2.append(True)
mylist2.append(My_list)
print(mylist2)
print("#"*50)

#Extends:
print("Extending: ")
list1=[1,2,3,4,5]
list2=["A","B","C"]
list3=["one","Two"]
list1.extend(list2)  #put list2 inside list1
list1.extend(list3)
list3.extend(list2)
print(list1)
print(list3)
print("#"*50)

#remove

list1.remove(2)
print("Removing: "+ str(list1))

#sort
list4=[1,25,80,2,44,564]
list4.sort() #removing one item
print("Sorting: " + str(list4))

#reverse
list4.sort(reverse=True) #Sorting from reverse
print("Reverse Sorting: "+ str(list4))

#clear
list5=[1,2,3,4,5,6,6]
list5.clear()
print("clearing : "+ str(list5))

#copy
list6=[1,2,3,"hello","hello"]
list7=list6.copy()
print("This is list 7 that is a copy from list 6: "+str(list7))
#count
print("The count of the 'hello' word is "+str(list7.count("hello")))

#index
print("The index of the word 'hello' are : " + str(list7.index("hello")))
#pop
print("Poping  the word 'hello' : " + str(list7.pop(3)))
#insert
print("inserting   the word 'World' : " + str(list7.insert(4,"world")))
print(list7)
print("Poping  the word 'world' : " + str(list7.pop(-1)))
print(list7)

print("#"*50)
print(" ")

#Tuples
tuple1=("1","nmaa","hawary")
tuple2="2","hind","assaf",
print(type(tuple2))
#tuple2[4]="hind" it doesn't support items assignmnts
print(tuple2[-1])
print("#"*50)
print(" ")
#Tuples methodes
#index
print(tuple1.index("nmaa"))
#len :is to find  how many items in the tupels starting from 0
print(len(tuple1))
#concanonations
tuple3=tuple1+tuple2
print(tuple3)

#Repeat for String , List , Tuples
String=" nmaa "
list8=[1,2]
tuple4=("A","B")

print( String* 4)
print(list8* 4)
print(tuple4* 4)

print("#"*50)
print(" ")
#Set
set1={"osama","ahmad","anas",(1,3),True}
print(type(set1))
print(set1)
#print(set1[0]) #not orderd and not indexing
#print(set1[0:4])  #slicing can't be done
#It has immutable data types : So can't have list : unhashable type 'list'2.c

#Set Methodes: 27
set2={1,2,3,4}
set3={"a","b","c"}
set4={"1","3","0"}
#clear methode 
print(set2.clear())
#union methode is like to extend the set
print(set4.union(set2,set3))
#add methode to the set
print(set3.add("nmaa"))
print(set3)
#remove from the end 
set3.remove("nmaa")
print(set3)

#discard : to delet spasfic items
set3.discard("n")
set3.discard("b")
print(set3)

#pop : pop items randomly 
i={"A","b",1,2,3,4,True}
print(i.pop())

#update
set3.update({"nmaa","welcome"})
set3.update(["Taisser","alhawary"])
print(set3)
print("#"*50)

#differences():  a-b 
a={1,2,3,4,5}
b={1,2,3,"nmaa","hawary"}
print(a.difference(b)) # that is in a and not in b
print(a)
print("#"*50)
#differences_update():  a
c={1,2,3,4,5}
d={1,2,3,"nmaa","hawary"}
print(c)
c.difference_update(d) # that is in c and not in d but it must be updated in c 
print(c)
print("#"*50)

#intersection() the common item 
e={1,2,3,4,"X","hiba"}
f={"Osama","B",2}
print(e)
print(e.intersection(f))
print(e)
print("#"*50)
#intersection() the common item 
g={1,2,3,4,"X","hiba"}
h={"Osama","B",2}
print(g)
print(g.intersection_update(h))
print(g)
print("#"*50)
#symmertic_diffrence()  ::which is to find the diffrence between them from the both side
k={1,2,3,4,5,67,"x"}
l={"X","hiba",1,2,3,4}
print(k)
print(k.symmetric_difference(l))
print(k)


print("#"*50)
#symmertic_diffrence_update()
j={1,2,3,4,5,67,"x"}
o={"X","hiba",1,2,3,4}
print(j)
j.symmetric_difference_update(o)
print(j)
print("#"*50)

#isupperset()
A={1,2,3,4}
B={1,2,3}
C={1,2,3,4,5,6}
D={11,21,34}

print(A.issuperset(B))
print(A.issuperset(C))
print(C.issuperset(B))
print(C.issuperset(A))
print("#"*50)
#issubset()
print(A.issubset(B))
print(A.issubset(C))
print(B.issubset(C))
print(A.issubset(C))
print("#"*50)
#isdisjoint()
print(A.isdisjoint(D))
print(D.isdisjoint(A))
print(B.isdisjoint(C))
print(A.isdisjoint(C))


# #boolean 
# print(bool(False))
# print(bool([1,2,3]))
# print(bool(()))
# print(bool(""))

# #comparasions: 
# # &gt; grater than 
# # &lt; less than 
# # &gt;=  gratear and equals



# #37
# #User input
# input1=input("Enter youar name ?")
# print("My name is "+ input1.capitalize().strip())


# # if statments 41:

# uname=input("Enter your name please ").capitalize().strip()
# mname=input("Enter your middel name please ").capitalize().strip()
# lname=input("Enter your last name please ").capitalize().strip()
# if uname=="Nmaa" and mname=="taisser" and lname=="Hawary":
#     print(f" your name is {uname} and middel name is {mname} and the last name is {lname}")

# elif uname=="Nmaa" or mname=="taisser" or lname=="Hawary":

#   print("It is okay one of them correct")
# else:
#     print("please Enter your correct name")







