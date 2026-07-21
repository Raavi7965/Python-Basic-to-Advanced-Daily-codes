num1=10  #int
num2=12.5 # float
total= num1+num2 # float
#Automatically type conversion is done by python
print(total) 

bool1=True   # by default the numerical value of  True=1 and False=0
num=12
total1= bool1+num
print(total1)

bool2=False
num=12
total2= bool2+num 
print(total2)

# Str="7"
# num=5
# print(Str+num)  # It will give an error because we cannot add string and integer directly. We need to convert the string to an integer first.

com1=3+4j
n=10
print(com1+n)  # It will give an error because we cannot add complex and integer directly. We need to convert the integer to a complex number first.

com2=7+6j
u=7.77
print(com2+u) # It will give an error because we cannot add complex and float directly. We need to convert the float to a complex number first.

salary=25000
print(float(salary))  # converting integer to float

# TYPE CASTING
m=7.7
print(int(m)) # converting float to integer

# com=3+4j
# print(int(com)) # It will give an error because we cannot convert complex to integer directly. We need to convert the complex number to a float first.

a=10
print(complex(a)) # converting integer to complex

Price=199
print(str(Price)) # converting integer to string
print(type(str(Price)))

list1=[10,20,30,40,50]
print(tuple(list1)) # converting list to tuple


# m=10
# print(dict(m)) # It will give an error because we cannot convert integer to dictionary directly. We need to convert the integer to a list of tuples first.


list=[10,20,30,40,50]
print(set(list)) # converting list to set











