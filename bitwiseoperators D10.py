# Bitwise AND (&)
a = 5
b = 3

print(a & b)

# Bitwise OR (|)
a = 5
b = 3

print(a | b)

# Bitwise XOR (^)
a = 5
b = 3

print(a ^ b)

# Bitwise NOT (~)
a = 5

print(~a)

# Left Shift (<<)
a = 5

print(a << 1)


# Right Shift (>>)
a = 5

print(a >> 1)


a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


number = 7

if number & 1:
    print("Odd number")
else:
    print("Even number")


#Bitwise operators:
#Bitwise and(&):
print(3&4)

#Bitwise or(|):
print(3|4)

#Bitwise xor(^):
print(3^4)

#Bitwise not(~):
print(~3)

#Note: computers doesn't store negative numbers in binary format, so the output of the bitwise not operator is -4.

#Bitwise left shift(<<):
print(3<<1)

#Bitwise right shift(>>):
print(3>>1)