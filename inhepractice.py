class Person:

	def __init__(self,first,last):
		self.first = first
		self.last  = last 
		self.depNum = 101
	
	def __str__(self):
		return self.first + "  " + self.last + " from department number " + str(self.depNum)
		
class Employee(Person):
	
	def __init__(self,first,last,age):
		Person.__init__(self,first,last)
		self.age = age
		
	def __str__(self):
		return Person.__str__(self) +  " your age is " + self.age
		
print(Person("amit","kumar"))
print(Employee("rahul","srivastava","26"))

		