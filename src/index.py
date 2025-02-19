# Printing  Basics in Python

print("Skills USA 2025")



# Variables in Python

firstName = "Bobby";      # declared firstName  with the value of Bobby
middleInitial = 'R';      # declared middleInitial  with the value of R
lastName = "Hill";        # declared lastName  with the value of Hill
age = 16;                 # declared age with the value of 16
isAStudent = True;        # declared isAStudent  with the value of true
hasAJob = False;          # declared hasAJob  with the value of false


# constants in Python

GRAVITY = 9.8   # Do not change gravity!


# Types in Python

school = "Central Georgia Technical College"     #Type would be String
GPA = 3.21                                       #Type would be Float
isATeacher = False                               #Type would be Boolean
age = 20                                         #Type would be Int

students = [];                                   #Type would be List

def print():                                    # Type would be function
    print("Hello")

thistuple = ("apple", "banana", "cherry", 7, True)  #Type would be Tuple 
                #Tuples are unchangebale like constants and hold diffrent types

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}                                                    #Type would be Dictionary
print(thisdict["brand"])                             #Dictionaries are used to store data values in key:value pairs.
                                                     #A dictionary is a collection which is ordered

fruits = {'apple', 'banana', 'cherry'}               #Type would be Set (most siimilar to array)





            #Arithemetic Expressions

friends = 20

friends = friends + 1;    # adding 1  this will give you 21
friends = friends - 1;    # subtracting 1  this will give you 20
friends = friends * 2     # multiplying by 2  this will give you 40
friends = friends / 2     # diving by 2  this will give you 20

# augment assingment operator  (shortcut)

friends +=1;        # adding 1  this will give you 21
friends -=1;        # subtracting 1  this will give you 20
friends *=2;        # multiplying by 2  this will give you 40
friends /=2;        # diving by 2  this will give you 20


            #String Expressions

snack = "Cheetos"

for x in snack:                                  #Loops through String and Prints each Character
    print(x)

print(len(snack))                                #Prints Length of String

txt = "Im happy today!"                          #Checks if a phrase is included in String
print("today" in txt)

txt = "The best things in life are free!"        #Checks if a phrase is NOT included in String
print("expensive" not in txt)

print(txt.upper())                              #Uppercases the String 
print(txt.lower())                              #Lowercases the String

a = "Good"                                     #Concatenate the string (combines)
b = "Morning"
c = a + b

name = "Bobert"                                 #String Format
msg = "My name is " + age 

lotteryNumber =  5763                           #FStrings  (Similar to C )
msg2 = f"Winning Number is {lotteryNumber}"


price = 100                                     #PlaceHolder (Similar to Javascript)
msg3 = f"The price is {price} dollars"                

                                                #A modifier is included by adding a colon :
                                                #followed by a legal formatting type, like .2f 
msg4 = f"The price is {price:.2f} dollars"      # which means fixed point number with 2 decimals:






            # List Expressions

thislist = ["apple", "banana", "cherry"]            #Would print bananna 
print(thislist[1])                                  #first index is 0

thislist = ["apple", "banana", "cherry"]             #Return item if it exist in list
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"                        #Changes item in list
   
thislist.insert(2, "watermelon")                    #Insert item without changing any items

thislist.append("orange")                           #Adds item at the end of list
  
thislist.remove("banana")                           #Remove item from list

thislist = ["apple", "banana", "cherry"]            #Adds elements of another list to list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

thislist = ["apple", "banana", "cherry"]            #Loops through List
for x in thislist:
  print(x)


                            #Tuple Expressions

thistuple = ("apple", "banana", "cherry")              #Access tuple element, would print bananna
print(thistuple[1])


y = ("orange",)                                        #Add a new element to tuple
thistuple += y

thistuple = ("apple", "banana", "cherry")               #Deletes tuple
del thistuple


thistuple = ("apple", "banana", "cherry")               #Loop through tuple
for x in thistuple:
  print(x)



                #User Input
username = input("Enter username:")
print("Username is: " + username)