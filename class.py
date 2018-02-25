
class Test:
	def __init__(self, name=None):
		print("Initial method has been called")
		self.name = name
	
	def say_hi(self):
		if self.name:
			print("Hello ! " + self.name + " Good Morning. ")
		else:
			print("Hello ! there, Good Morning")
	
	def get_name(self):
		return self.name
	
	def set_name(self, name):
		self.name = name
	
x = Test()	
#x.name = "Ankit"
#x.say_hi()
print(x.get_name())
print()
x.set_name("Rahul")
print(x.get_name())