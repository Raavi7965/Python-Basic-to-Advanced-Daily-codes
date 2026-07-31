# Write a Program to withdraw money from my account

withdraw = int(input('Enter the amount to withdraw: '))
balance = 10000
if withdraw<=balance:
    balance-=withdraw
    print(f'with draw sucessful and current balance {balance}')
else:
    print('Not enough balance')
    
    
    
    # Write a aprogram to check whethen a person can login or not 
    
password = input('Enter your password: ')
savedpassword = 'vk@admin'

if password == savedpassword:
    print("Login Successfully")
else:
    print("Login password is incorrect")
        
# Conditional Statements with logical operators

empid = [101,102,103,104,105]
fingerprint=input('Enter whether the finger print is valid or not: ')
empid=int(input('Enter employee id: '))
if fingerprint=='valid' and empid in empid:
    print('Employee is present')
else:
    print('not Employee ')
    
# Write a program to check loan eligibility based on salary and cibil score

salary = int(input("enter the salary : "))
cibil = int (input("enter the cibil score: "))
if salary >= 60000 and cibil >= 750:
    print('customer is eligible for loan')
else:
    print('Customer did not match the loan eligibility criteria')
    

# or operator 

graduation = input('Enter your qualification: ')
if graduation=='degree' or graduation =='btech':
    print('you are meeting the application criteria')
else:
    print('Job criteria did not match')
    
    
