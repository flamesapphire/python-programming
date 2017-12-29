import math
x=input("enter the no x")
y=input("enter the no y")

print x
print y

z=y+x
z=math.ceil(z)


if z%2==0:
	print "even"

elif z%2==1:
	print "odd"

else:
	print "lol"
