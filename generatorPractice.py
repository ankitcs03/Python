
def fibonacci(n):
	"""This function return the fibonacci series till the n number """
	a, b, counter = 0 ,1, 0 
	while True:
		if (counter > n):
			return
		yield a
		a, b, counter = b, a+b, counter+1
		

f = fibonacci ( 5 )

for x in f :
	print(x, " ", end="" )
print()