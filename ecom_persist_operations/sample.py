


class Employee:

    def __init__(self,eid,enm,eag,esal,erole,eadr):
        self.empId = int(eid)
        self.empName = enm
        self.empAge = int(eag)
        self.empSalary = float(esal)
        self.empRole = erole
        self.empAddress = eadr

    def __str__(self):
        return f'''\n\n {self.__dict__}'''

    def __repr__(self):
        return str(self)



class Role:
    def __init__(self,rid,rcode,rname):
        self.roleId = rid
        self.roleCode = rcode
        self.roleName = rname

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

class Address:
    def __init__(self,city,state,pincode):
        self.city = city
        self.state = state
        self.pincode = pincode

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)


import random
ROLESLIST = ['SSE','SE','MANAGER','CEO','STAFF','HOUSKEEPING','LEAD']

role_count = 0
def get_dummy_role():
    global role_count
    role_count = role_count + 1
    ROLE = ROLESLIST[random.randint(0,len(ROLESLIST)-1)]
    return Role(rid=role_count,rcode=ROLE+str(role_count),rname=ROLE)

adr_count = 100
ADDRESSLIST = ['PUNE','MUMBAI','SATARA','SANGLI','KOLHAPUR','LATUR','NANDED','ANAGAR','BEED']
def get_dummy_address():
    global adr_count
    adr_count = adr_count + 1
    city = ADDRESSLIST[random.randint(0, len(ADDRESSLIST) - 1)]
    return Address(city,state='MH',pincode=random.randint(111111,999999))

emp_count = 770
def get_dummy_employee(n):
    global emp_count
    emp_count = emp_count + 1
    emplist = []
    for item in range(n):
        name = f'{chr((random.randint(65,90)))}AAAA'
        age = random.randint(22,60)
        salary = round(random.randint(30000,80000)/3,2)
        adrlist = []
        for adr in range(random.randint(1,5)):
            adrlist.append(get_dummy_address())

        roles = []
        for adr in range(random.randint(1,3)):
            roles.append(get_dummy_role())

        emplist.append(Employee(eid=emp_count,enm=name,eag=age,esal=salary,erole=roles,eadr=adrlist))
    return emplist
emplist = get_dummy_employee(10)

'''
python --> text/csv/excel/json/xml/yaml -> serialization--------------> python ---. deserialization
                    
Serialization -->  process of converting lang object [python] --> into network supported [bytes]/file supported
Deserialization --. opps of serialization

'''
import os
import json

FILEPATH = os.getcwd() + "\\empdata.json"
def write_data_into_json():
    empdictlist = []
    for emp in emplist:         #emp[101,AAA,rolelist[role1[id,code,name],role2],addreslist[adr1,adr2]]
        adrlist = []
        for adr in emp.empAddress:
            adrlist.append(adr.__dict__)

        rolelist = []
        for role in emp.empRole:
            rolelist.append(role.__dict__)


        empdict = emp.__dict__
        empdict['empAddress'] = adrlist
        empdict['empRole'] = rolelist
        empdictlist.append(empdict)

    empjson = json.dumps(empdictlist)

    with open(FILEPATH,'w') as file:
        file.writelines(empjson)


#write_data_into_json()

def read_data_from_json():
    with open(FILEPATH,'r') as file:
        empcontents = json.load(file)

        for emp in empcontents:
            adrlist = emp.get('empAddress')
            for adr in adrlist:
                if adr.get('city') == 'NANDED':
                    print(emp.get('empId'),emp.get('empName'), adr.get('city'))

read_data_from_json()
