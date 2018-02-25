
def our_decorator(func):
	def function_wrapper(x):
		print("Before calling the function " + func.__name__)
		func(x)
		print("After calling the function " + func.__name__)
	return function_wrapper

@our_decorator
def foo(x):
	print("function is called with string " + str(x))

foo(25)
