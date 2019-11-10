encoder_caesar = {'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}

def cipher(string):
	for i in range(len(string)):
		print(encoder_caesar[i])
		

lol="lol"
meet=cipher(lol)
print(meet)