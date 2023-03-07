#Task1
#Enter Two input with a promt and calculate them +,* and - 

input1=input("Please enter input1 with the symbol:")
input2=input("Please enter input2:")
input3=[input2]

if "+" in input1:
  list1=input1.split("+")
  list1.append(input2)
  print(list1)
  sum=int(list1[0]) + int(list1[2])
print(sum)

#Task2 : Enter one input with a promt and calculate them +,* and - 
x=input("Enter numbers:")
if "+" in x:
 list=x.split("+")
 print(list)
 result=int(list[0])+int(list[1])
 print(f"The summation is :{result}")
elif "*" in x:
  list=x.split("*")
  print(list)
  result=int(list[0])*int(list[1])
  print(f"The multiplation is :{result}")
elif "-" in x:
  list=x.split("-")
  print(list)
  result=int(list[0])-int(list[1])
  print(f"The substraction is :{result}")  

else:
    print("invalid")  
