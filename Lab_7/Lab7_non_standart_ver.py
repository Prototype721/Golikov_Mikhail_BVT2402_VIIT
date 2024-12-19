class Employee:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.salary = data['salary']
        #super().__init__(**kwargs)

    def get_info(self):
        return (self.name, self.id, self.salary)
    

class Manager(Employee):
    def __init__(self, data):
        super().__init__(data)
        self.department = data['department']
    
    def get_info(self):
        return (*super().get_info(), self.department)
        
    
    def get_department(self):
        return self.department
    
    def manage_project(self):
        return "Managing project in progress..."
    

class Technician(Employee):
    def __init__(self, data):
        super().__init__(data)
        self.specialization = data['specialization']

    def get_info(self):
        return (*super().get_info(), self.specialization)
        
    
    def get_specialization(self):
        return self.specialization
    
    def perform_maintenance(self):
        return "Performing maintenance..."
    

class TechManager(Manager, Technician):

    def __init__(self, data):
        
        super().__init__(data)
        self.team_list = []

    def get_info(self):

        info = super().get_info()
        return info
    
    def add_employee(self, employee):
        self.team_list.append(employee)

    def get_team_info(self):
        for employee in self.team_list:
            print(employee.get_info())
        
        return True








data = {
    'name' : 'Mike', 
    'id' : '1',
    'salary' : '13000',
    'department':'Research',
    'specialization':'Electric'

}

My_TechManager = TechManager(data)

print('\n')
print(My_TechManager.get_info(), end ='\n\n')

print(My_TechManager.manage_project(), end ='\n\n')

print(My_TechManager.perform_maintenance(), end ='\n\n')


dat1 = {
    'name':'Jane Doe', 
    'id' : '2',
    'salary':'Unknown',
    'department':'FSB'
}

dat2 = {
    'name':'JoHn Doe', 
    'id' : '3',
    'salary':'Unknown',
    'specialization':'Hacker'
}
Worker_1 = Manager(dat1)

Worker_2 = Technician(dat2)


My_TechManager.add_employee(Worker_1)
My_TechManager.add_employee(Worker_2)


My_TechManager.get_team_info()