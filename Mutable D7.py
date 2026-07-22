int1 =10
print(int1) # it will give the value of int1

list=[1,2,3,4,5]
print(list) # it will give the value of list
print(id(list)) # it will give the id of list

int2=10
print(int2) # it will give the value of int2
print(id(int2)) # it will give the id of int2
int2=5
print(int2) # it will give the value of int2
print(id(int2)) # it will give the id of int2

# Check the imutability for float and complex
flt1=12.5
print(flt1) # it will give the value of flt1
print(id(flt1)) # it will give the id of flt1
flt1=15.5
print(flt1) # it will give the value of flt1
print(id(flt1)) # it will give the id of flt1


# Since set and dict are unordered we cammot use += for them.
set1={'sumanth','venkatesh','uma','abishay','akash'}
print(set1) # it will give the value of set1
print(id(set1)) # it will give the id of set1
set1|={'srinivas','Bose','Vijay'}
print(set1) # it will give the value of set1
print(id(set1)) # it will give the id of set1


dict1={'name':'venkatesh','age':28,'city':'Bangalore', 'gender': 'male'}
print(dict1) # it will give the value of dict1
print(id(dict1)) # it will give the id of dict1


# INPUT FUNCTION()
#By default input takes values as string
name=input("Enter your name: ") # it will take the input from the user
print(f'Hello {name},welcome to python programming') # it will print the name of the user


num1=int(input("Enter your first number: ")) 
num2=int(input("Enter your second number: ")) 
print(num1+num2)


#CHECKING ARITHMETIC OPERATORS


num1=int(input("Enter your first number: ")) 
num2=int(input("Enter your second number: ")) 
print(num1+num2)
print(f'The sum of {num1} and {num2} is {num1+num2}')
print(f'The difference of {num1} and {num2} is {num1-num2}')
print(f'The Multiplication of {num1} and {num2} is {num1*num2}')
print(f'The Division of {num1} and {num2} is {num1/num2}')
print(f'The Floor Division of {num1} and {num2} is {num1//num2}')
print(f'The Modulus of {num1} and {num2} is {num1%num2}')
print(f'The Exponent of {num1} and {num2} is {num1**num2}')
print(f'The Exponent of {num2} and {num1} is {num2**num1}')
print(f'The Exponent of {num1} and {num1} is {num1**num1}')
print(f'The Exponent of {num2} and {num2} is {num2**num2}')
print(f'The Exponent of {num1} and {num2} is {pow(num1,num2)}')
print(f'The Exponent of {num2} and {num1} is {pow(num2,num1)}')


