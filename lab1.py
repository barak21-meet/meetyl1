import math
#1
num1=input("Please put a number between 1 to 10  ")
num2=input("Please put another number between 1 to 10  ")
#2
num1=int(num1)
num2=int(num2)
n1_pow_by_n2=math.pow(num1,num2)
n2_pow_by_n1=math.pow(num2,num1)
print (n1_pow_by_n2)
print (n2_pow_by_n1)
#3
num3=num1+num2
num3_square=math.sqrt(num3)
num4=num3
print (num3_square)
"""
n1_square=num1.sqrt(num1)
n2_square=num2.sqrt(num2)
print (n1_square)
print (n2_square)
"""
#4
while num3_square<100000:
	num3_square+=1
print (num3_square)

#Bonus
while num4>0:
	num4-=1
num4+=100000
print (num4)
