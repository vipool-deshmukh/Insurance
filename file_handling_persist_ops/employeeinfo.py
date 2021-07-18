



class Employee:

    def __init__(self,eid,empnm,eag,egen,emsal,erole,eaddrs):
        self.empId = int(eid)
        self.empName = empnm
        self.empGender = egen
        self.empSalary = float(emsal)
        self.empAge = int(eag)
        self.empRole = erole
        self.empAddress = eaddrs

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.empId} \t\t {self.empName}\t\t{self.empGender}\t\t{self.empAge}\t\t{self.empRole}\t\t{self.empSalary}\t\t{self.empAddress}\n'''

    def __eq__(self, other):
        return self.empId == other.empId


import random
GENDER = ['M','F']
ROLES = ['SSE','SE','MANAGER']
ADDRESS = ['PUNE','MUMBAI','CHENNAI']
count = 100
def dummy_data():
    global count
    count = count + 1
    return Employee(eid = count,empnm=f'{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}A{count}',eag=random.randint(22,45),
                    egen=GENDER[random.randint(0,1)],emsal=random.randint(10000,30000),
                    erole=ROLES[random.randint(0,2)],eaddrs=ADDRESS[random.randint(0,2)])

def get_num_emps(n):
    return [dummy_data() for item in range(n)]


#ans = get_num_emps(100)
#print(ans)

