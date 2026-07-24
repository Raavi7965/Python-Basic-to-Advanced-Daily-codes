# Logical Operators
# AND

age = 21
citizen = 'Indian'
print(age>18 and citizen=='Indian')


# OR
degree=True
btech=False
print(degree or btech)

# Checking whether it is a holiday based on weekend or festive day 

weekend = False
festiveday=True
print(weekend or festiveday)

# Payment with cash or card or upi

card ='No'
cash = 'Yes'
upi = 'Yes'
print(card=='Yes' or cash=='Yes' or upi=='Yes')

#not
age = 20
print(not age < 18)  # True, negates the condition

## IDENTITY OPERATORS
#IS

num1=10
num2=10
print(num1 is num2)

# IS NOT 

developer='writes code'
tester='test code'
print(developer is not tester )

nu1 = 10
nu2=10.1
print(nu1 is not nu2)

# Code Optimization : The Program creats only on object for all variables if the object size is within
# limit if the size of the object goes beyyond that limit python creates diffrent objects for diffrent variables

list1=[1,2,3,4,5]
print(id(list1))
list2=[1,2,3,4,5]
print(id(list2))
print(list1 is list2)

# MEMPERSHIP OPERATOR
#IN
names=['venkatesh','sumanth','uma','abishay','akash']
print('bose' in names)
print('venkatesh'in names)

# NOT IN 
names=['venkatesh','sumanth','uma','abishay','akash']
print('bose' not in names)
print('venkatesh'not in names)
