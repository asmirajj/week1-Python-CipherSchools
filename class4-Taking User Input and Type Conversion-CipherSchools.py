#Taking User Input

#Delimiter is \n character

a=input()
print(a)
print(type(a))

#Sample python code

a=input()
b=input()
print(a)
print(b)

#Input in python is delimited using \n by default

#Type Casting
a=65
print(bin(65))


#Typecoercion
#To do type concersion we use coersioning
a=15
print(str(a))
print(int('12345'))
print(float('1.5'))


#Python doesn't have type casting
a=65
j=isinstance(a,object)
a='A'
l=isinstance(a,object)

print(j,l)

