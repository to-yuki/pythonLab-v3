# Class Defin.

class Employee(object):  # Super Class
	
	__money=0

	def base(self,base):
		self.__money=base

	def pay(self):
		print('Total Salary Pay --> ' +str(int(self.__money)))


class Manager(Employee):  # Class Inheritance(Sub Class)
	def base(self,base):
		super(Manager,self).base(base*1.5) # Super Class call method.

objs = [Employee(),Manager()]

for o in objs:
	print('--------------')
	print('pay():'),
	o.base(300000.0)  # Polymorphism Code
	o.pay()

