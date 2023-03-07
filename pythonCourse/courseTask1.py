# First : Task -only for "print" 
print ("Hello  my faviort land ")
print ("#"*50)

# Second :Comments 
print("hello my faviout words") #Inline comment 

""" multible 
line 
comment""" 

# Third: methodes type to knowing the data types: 

print(type ("hello")) #String
print(type(100))  #integer
print(type(70.77)) #float
print(type([1,2,3,4])) #list
print(type(("nmaa","hawary"))) #Tupel 
print(type({1,2,3,4}))  #Set
print(type(True))  #boolean
print(type({"one":1, "Two":2})) #Dictionary- key:value
print ("#"*50)

#Four : Recived words :

help("keywords")

#Exapmpels: 
name= "nmaa"
age=15
school="HTU"
print(f"My name is {name.capitalize()} and my age is {age} and my school is {school.lower()}")
#OR
name, age, school ="Huda",19,"NUA"
print(f"My name is {name.capitalize()} and my age is {age} and my school is {school.lower()}")
print ("#"*50)

#Escapes: Charachters

# \b : back Space
print("Hello\bWord")

# \newLine  , or \ 
print ("My name is : nmaa\
 Taiseer\
 hawary")

# Escape backslash \\ 
print ("my age is  \\ 20")

# \' Escape single quote
print ("I'm studing CS at \'HTU\'")

# \" Escape double quote
print ("My GPA is  \"3.77\"")

# \n line feed  
print ("It was a nice\n major")

# \r carriage returen 
print ("Good\rbye")

# \t hirozantal tap 
print ("I love python \t so much")

# \xhh : Hhex value 
print ("I born in \x4F\x32")

print ("#"*50)

#Concatenaten And Traning 
print("Hello my world" + " " + "\n" + f"My name is {name.capitalize()}")
print("I like swimming 'but' I do not know hoe to swim")
#print("my age is" + 23) Erorr can't concatonate numbers with Str

print ("#"*50)
#Slicing And Indexing:

My_String ="Hello my World"
print(My_String)
print(My_String[0]) #"Starting"
print(My_String[2])
print(My_String[-1]) #"End"
print(My_String[-2])
print("My slicing from 0-3 : "+ My_String[0:3])
print("My slicing from 0-5 : "+ My_String[:5])
print("My slicing from 3 to -1 : "+ My_String[3:])
print("My slicing from 0-3 with two steps: "+ My_String[3::2]) #"End" with steps 
print ("#"*50)
#Strings Methodes 13: 
# strip() , Capitilize() , rstrip() , lstrip() , zfill(), Upper(), lower(), Title()
String="######welcome to the worlds#####"
A="welcome maam"
a,b,c,d="1","23","400","11"
My_name="hanadi"
Lower="NMAA"


print(String.strip("#")) #Rempve space from begining and the end 
print(String.rstrip("#")) #Rempve space from the end 
print(String.lstrip("#")) #Rempve space from begining 

print("Here is in an capitalize case: "+ A.capitalize()) #Capitilize the first letter
print("Here is in an Title case: "+ A.title()) #Title() capitileze the first letter of each word
print("Here is in an upper case: "+ My_name.upper())
print("Here is in an lower case: "+ Lower.lower())
print(a.zfill(2))  
print(b.zfill(3)) #methodes tp pades strings with zeroes to spicified width
print(c.zfill(4))
print(d.zfill(5))
print ("#"*50)

















