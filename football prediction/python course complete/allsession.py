#Python course chapter No: 1
#1. Python output:
 #Python is a case sensitive language
for i in range (1,100):
   print("dkfjdkf")

print('Hello World')
print('Salman khan')
#2. Data types:
 #Integer
print(8)
1*10^308
print(1e309)
 #Decimal/Float
print(8.55)
#print(1.7e309)
#Boolean
print(True)
print(False)
 #Text/String
print('Hello World')
 #complex
print(5+6j)
 #List-> C-> Array
print([1,2,3,4,5])
# Tuple
print((1,2,3,4,5))
# Sets
print({1,2,3,4,5})
# Dictionary
print({'name':'Nitish','gender':'Male','weight':70})
 #type
type([1,2,3])
# Dynamic Typing
a = 5
 #Static Typing
 #int a = 5
 #Dynamic Binding
a = 5
print(a)
a = 'nitish'
print(a)

# Static Binding
#int a = 5

a = 1
b = 2
c = 3
print(a,b,c)
a,b,c = 1,2,3
print(a,b,c)
a=b=c= 5
print(a,b,c)
#3. Comments
 #this is a comment
 #second line
a = 4
b = 6 # like this
# second comment
print(a+b)
#4. Keywords & Identifiers
 #Identifiers
 #You can't start with a digit
name1 = 'Nitish'
print(name1)
#You can use special chars -> _
_ = 'ntiish'
print(_)
#identiers can not be keyword
#________________________________________
#Temp Heading
#________________________________________
#5. User Input
 #Static Vs Dynamic
input('Enter Email')
 #take input from users and store them in a variable
fnum = int(input('enter first number'))
snum = int(input('enter second number'))
print(type(fnum),type(snum))
 #add the 2 variables
result = fnum + snum
# print the result
print(result)
print(type(fnum))
#6. Type Conversion
 #Implicit Vs Explicit
print(5+5.6)
print(type(5),type(5.6))

print(4 + '4')
# Explicit
# str -> int
#int(4+5j)

# int to str
str(5)

 #float
float(4)
#7. Literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)
#binary
x = 3.14j
print(x.imag)
string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(raw_str)
a = True + 4
b = False + 10

print("a:", a)
print("b:", b)
k = None
a = 5
b = 6
print('Program exe')

#-----------------------Session 2------------------------------------------------------------------
# Arithmetric Operators
print(5+6)

print(5-6)

print(5*6)

print(5/2)

print(5//2)

print(5%2)

print(5**2)
# Relational Operators
print(4>5)

print(4<5)

print(4>=4)

print(4<=4)

print(4==4)

print(4!=4)
# Logical Operators
print(1 and 0)

print(1 or 0)

print(not 1)


# Bitwise Operators

# bitwise and
print(2 & 3)

# bitwise or
print(2 | 3)

# bitwise xor
print(2 ^ 3)

print(~3)

print(4 >> 2)

print(5 << 2)
# Assignment Operators

# = 
# a = 2

a = 2

# a = a % 2
a %= 2

# a++ ++a

print(a)
# Membership Operators

# in/not in

print('D' not in 'Delhi')

print(1 in [2,3,4,5,6])
# Program - Find the sum of a 3 digit number entered by the user

number = int(input('Enter a 3 digit number'))

# 345%10 -> 5
a = number%10

number = number//10

# 34%10 -> 4
b = number % 10

number = number//10
# 3 % 10 -> 3
c = number % 10

print(a + b + c)
# login program and indentation
# email -> nitish.campusx@gmail.com
# password -> 1234

email = input('enter email')
password = input('enter password')

if email == 'nitish.campusx@gmail.com' and password == '1234':
  print('Welcome')
elif email == 'nitish.campusx@gmail.com' and password != '1234':
  # tell the user
  print('Incorrect password')
  password = input('enter password again')
  if password == '1234':
    print('Welcome,finally!')
  else:
    print('beta tumse na ho paayega!')
else:
  print('Not correct')
# min of 3 number

a = int(input('first num'))
b = int(input('second num'))
c = int(input('third num'))

if a<b and a<c:
  print('smallest is',a)
elif b<c:
  print('smallest is',b)
else:
  print('smallest is',c)
# menu driven calculator
menu = input("""
Hi! how can I help you.
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawl
4. Enter 4 for exit
""")

if menu == '1':
  print('pin change')
elif menu == '2':
  print('balance')
else:
  print('exit')
	# Loops in Python
#Loops in Python
	#Need for loops
	#While Loop
	#For Loop
	# While loop example -> program to print the table
	# Program -> Sum of all digits of a given number
	# Program -> keep accepting numbers from users till he/she enters a 0 and then find the avg
  
number = int(input('enter the number'))	
i = 1
	
while i<11:
	print(number,'*',i,'=',number * i)
i += 1
	# while loop with else 
	
x = 1
	
while x < 3:
	print(x)
	x += 1
else:
    print('limit crossed')

# Guessing game

# generate a random integer between 1 and 100
import random

jackpot = random.randint(1,100)

guess = int(input('guess karo'))
counter = 1
while guess != jackpot:
  if guess < jackpot:
    print('galat!guess higher')
  else:
    print('galat!guess lower')

  guess = int(input('guess karo'))
  counter += 1

else:
  print('correct guess')
  print('attempts',counter)

  

# For loop demo

for i in {1,2,3,4,5}:
  print(i)
#Program - The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years.
curr_pop = 10000

for i in range(10,0,-1):
  print(i,curr_pop)
  curr_pop = curr_pop - 0.1*curr_pop



