class Employee:
    id = 0
    def __init__(self,name:str)->None:
        self.name = name
        Employee.id+=1
        self.id = Employee.id

    def get_info(self)->str:
        return f'Имя работника:{self.name}, id работника:{self.id}'


class Manager(Employee):
    def __init__(self, name: str, department: str)->None:
        super().__init__(name)
        self.department = department
        self.id = Employee.id
        self._manage_project = []

    def add_manage_project(self,project:str)->None:
        self._manage_project.append(project)

    def manage_project(self)->list:
        return self._manage_project

    def get_info(self)->str:
        return f'Имя работника:{self.name}, id работника:{self.id}, департамент:{self.department}'


class Technician(Employee):
    def __init__(self, name: str, specialization: str)->None:
        super().__init__(name)
        self.specialization = specialization
        self.id = Employee.id
        self.completed_task = []

    def perform_maintenance(self,task:str)->None:
        self.completed_task.append(task)

    def get_info(self)->str:
        return f'Имя работника:{self.name}, id работника:{self.id}, департамент:{self.specialization}'


class TechManager(Manager, Technician):
    def __init__(self, name: str, department:str, specialization: str) -> None:
        super(Manager,self).__init__(name, specialization=specialization)
        self.department = department
        self._managed_employees = []

    def get_info(self) -> str:
        return f'имя: {self.name}, id работника: {self.id}, департамент:{self.department}, специализация:{self.specialization}'

    def add_employee(self,empl:object)->None:
        self._managed_employees.append(empl)

    def get_info_team(self) -> list:
        return [[empl.get_info()] for empl in self._managed_employees]



empl1 = Manager('a',department = 'b')
empl2 = Technician('a1', specialization='c')
empl3 = Employee('a2')
empl4 = TechManager('a',department='c',specialization='d')
empl4.add_employee(empl1)
empl4.add_employee(empl2)
empl4.add_employee(empl3)
empl1.add_manage_project('add new employee')
empl1.add_manage_project('add new technician')
print(empl1.manage_project())
print(empl1.get_info())
print(empl2.get_info())
print(empl3.get_info())
print(empl4.get_info())
print(empl4.get_info_team())



