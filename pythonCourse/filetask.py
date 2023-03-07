import os
#MAIN DIRECITORY
# print(os.getcwd())

# print(os.path.abspath(__file__))
# The directory for the open file
print(os.path.dirname(os.path.abspath(__file__)))
#change directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

print("#"*50)

#path,name and mode
myFile= open("/home/nmaa/pythonCourse/file.txt","r")
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

print("#"*50)

#wiriting on the file
for i in range(100):
  myFile.write(f"{i} \n")

#Reading from the file:
print(myFile.read())
print(type(myFile.readlines()))
print("#"*50)

sum=0
with open("/home/nmaa/pythonCourse/file.txt","r")as f :
 for line in f:
  try:
    sum+= int(line)
  except ValueError:
     print("Erorr")
print(f"The total lines is: {sum}")
myFile.close()
