def CommonNum(list1,list2):
	Number=0
	for i in range (len(list1)):
		if list1[i] in list2:
			Number+=1

	return Number

list1=[20,30,40,50,80,213213,4325]
list2=[50,80,20,30,40,532,653,324]
Answer=CommonNum(list1,list2)

print(Answer)




"""
FIRSTTTT
def CommonNum(list1,list2):
	Number=0
	for i in range (len(list1)):
		if list1[0:-1]==list2[0:-1]:
			Number=Number+1
	return Number

list1=[2,5,6,8,9,8,4,6,7,3,2,5]
list2=[3,2,5,7,8,2,3]
Answer=CommonNum(list1,list2)
print(Answer)
"""


"""
SECONDDDDDDD
def CommonNum(list1,list2):
	Number=0
	for i in range (len(list1)):
		for b in  range (len(list2)):
			if i in list2:
				Number+=1
			if b in list1:
				Number+=1

	return Number

list1=[20,30,40,50,80,213213,4325]
list2=[50,80,20,30,40,532,653,324]
Answer=CommonNum(list1,list2)

print(Answer)
"""