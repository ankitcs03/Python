def test(arg1, *argv):
	print ("first argument is : ", arg1)
	for arg in argv:
		print ("next argument from argv is : ", arg)

test('ankit', 'srivastava', 'ankur', 'amit', 'abhishek')	

print ("\n\n")

def TestFinal(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.items():
			print ("key is", key,  "and value is ", value)
print ("Out from the loop")

variable={"Name" : "Anit", "Age":"29", "Contact":"843748329"}
TestFinal(**variable)
