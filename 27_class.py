# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:29:16 2020

@author: CEC
"""

class TheSimplestClasee:
    pass
miprimerobjeto=TheSimplestClasee()
misegundoobjeto=TheSimplestClasee()
mitercerbjeto=TheSimplestClasee()
micuartoobjeto=TheSimplestClasee()


class Empleado:
    empCount=0
    def __init__(self,name,salary,genero):
        self.name=name
        self.salary=salary
        self.genero=genero
        Empleado.empCount+=1
    def displayCount(self):
        print("Total Employee %d" % Empleado.empCount)
        
    def displayEmpleado(self):
        print("Name : ",self.name, ", Salary: ", self.salary, ", Genero", self.genero)

emp1 = Empleado("Zara",2000,"m")
emp2 = Empleado("Manni",5000,"h")
emp3 = Empleado("JOHA",2000,"m")
emp4 = Empleado("LU",5000,"h")

emp1.displayEmpleado()
emp2.displayEmpleado()
emp3.displayEmpleado()
emp4.displayEmpleado()
print ("Total Employee %d" % Empleado.empCount)



class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)


