#Code to print hello world in python
print("Hello")
print("Hello World!")

#this is a comment

a="a"
m=type(a)

print(m)

print(isinstance("a",str))
print(isinstance("a",int))
print(isinstance(2,str))
print(isinstance("a",object))
print(isinstance(2,object))
print(isinstance(print,object))

#Every line executed in python is either
 #1)Statement
 #2)Expression

a=255
print(a)
a="a"
print(a)
print(type(a))
print(id(a))
b=200
print(id(b))
c=278
print(id(c))

a="aaaaa"
print(id(a))
b="aaaaa"
print(id(b))

#id of a and b are same since the value provided to both the variables is same

a=5677453456754535246681255632435678456789765463
print(a+1)

#valid examples of identifiers
_a=12
a1=1
