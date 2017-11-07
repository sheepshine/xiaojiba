class Person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print 'hi, I\'m',self.name

p = Person('papapa')
p.sayHi()		

class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def tell(self):
		print 'Name:"%s" Age:"%s"' % (self.name, self.age)

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print 'name is %s' %(self.name)

	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: %s' %self.salary

t = Teacher('papa', 10, 160000)
t.tell()	

