class Employee():
    employeeCount=0
    totalSalary=0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount = Employee.employeeCount + 1
        Employee.totalSalary = Employee.totalSalary + Employee.getEmployeeSalary(self)
    def countEmployee(self):
        return Employee.employeeCount
    def getEmployeeName(self):
        return self.name
    def getEmployeeSalary(self):
        return self.salary
    def getAvgSal(self):
        return  Employee.totalSalary/Employee.employeeCount

class Manager(Employee):
    def __init__(self,name,salary):
        super(Manager,self).__init__(name,salary)

employee = Employee('Joy',10000)
print("Employee Name:"+employee.getEmployeeName())
print("Employee Salary:%d"%(employee.getEmployeeSalary()))
print("Total Employee:%d"%(employee.countEmployee()))
print("\n")

employee = Employee('Harry',12000)
print("Employee Name:"+employee.getEmployeeName())
print("Employee Salary:%d"%(employee.getEmployeeSalary()))
print("Total Employee:%d"%(employee.countEmployee()))
print("\n")

manager = Manager('Boss',14000)
print("Employee Name:"+manager.getEmployeeName())
print("Employee Salary:%d"%(manager.getEmployeeSalary()))
print("Total Employee:%d"%(manager.countEmployee()))
print("\n")

print("Avg sal is : %f" %(employee.getAvgSal()))