f=open("users.txt","a+")
for i in range(2):
	f.write("This is line %d\r\n"%(i+1))
f.close()

f.open("users.txt","r")
if f.mode=='r':
	content=f.read()
print(content)