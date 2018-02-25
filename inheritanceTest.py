class Person:
	
	def __init__(self, first,last):
		self.first = first
		self.last  = last
		
	def Name(self):
		return self.first + " " + self.last
		
class Employee(Person):
	
	def __init__(self, first, last, age):
		#super(Employee, self).__init__(first,last)
		Person.__init__(self,first,last)
		self.age = age
		
	def GetEmployee(self):
		return self.Name() + " age is " + self.age

E = Employee("ankit","srivastava","26")
print(E.GetEmployee());
	