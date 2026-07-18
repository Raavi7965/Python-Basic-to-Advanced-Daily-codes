# #Dictionary
a={'key':'value'}
print(type(a))
print(a)

# key value update 
v={'vr':'venkatesh','vr':'ap'}
print(v)

a.items()
print(a.items())

c={'name':'venkatesh','age':25,'address':'inkollu'}
print(c)

c.keys()
print(c.keys())

c.pop('address')
print(c)

f={'name':'Uma',
   'accountid':'SBI07821462',
   'amount':5000}
print(f)

f['amount']+=5000
print(f)

print(f['name'])

#Sets

d={1,2,3,4,5,6,5,6,7,8,9}
print(d)

#UNION

e={5,6,7,9,2,1,11,16}
print(d|e)

#Intersection
print(d&e)

#Difference
print(d-e)
 

