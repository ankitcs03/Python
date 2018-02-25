def B():
	print("Hi, Thanks for calling me.")
	print("Bye Bye!!!")



def A(func):
	print("Hi, I am first function section.");
	print("I am going to call another function from this function");
	func()
	print("Function real name is " + func.__name__);
	
A(B)