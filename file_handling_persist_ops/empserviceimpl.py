from file_handling_persist_ops.employeeinfo import Employee,get_num_emps
from file_handling_persist_ops.empservice import EmpService
import os       # PYTHON PROVIDED

#print(os.getcwd())  # get current working directory
#. --> current directory-->
'''
                        
                        w --> always new file --> write operation       --> 
                        r --> file required -- otherwise error --> read
                        a --> file present:data append --> file absent -- new file and the data write
                        x--> just to check file present or absent
                                                                    --> A
                                    X --SUCCESSFUL--> READ MODE
                                    X -- FAIL -- WRITE MODE-->
                                    
                        w+ --> read/write- -> new file 
                        r+ --> read/write  --> file shud be present.
                
                RESTAPI --> WEBSERVICES --> **
                        b --> multimedia --> FILE/image/audio/video/binarydata--> 
                                                                                        directory                                         remarks  

purpose                                             file already present                     file is absent                           
    r           --> only read mode                      works :read                            error --filenotfound               file required 
    w           --> only write mode                     overwrite :write                       new create :write          ->always new file create hot ahe
    r+          --> read+write mode                     works--read/write                       error
    w+          --> write+read mode                     overrwrite:read/write                 newcreate:read/write
    
 multimedia --> rest api-- webservices-->   
    rb           --> binary mode
    wb           --> binary format             
  
    x           -->                                      error                                     no error             --. just to check directory madhe file/present or absent
    a           --> append mode                         data append                             new file and then append
    a+          
    
    x --> repeat
    
'''

#D:\python_work\python_concepts\file_handling_persist_ops
COMMON_PATH = '\\empdata\\emp'
TEXT_FILE_PATH  = os.getcwd()+COMMON_PATH +".txt"       #STR
JSON_FILE_PATH  = os.getcwd()+COMMON_PATH +".json"      #STR
EXCEL_FILE_PATH = os.getcwd()+COMMON_PATH +".xlsx"      #STR
XML_FILE_PATH = os.getcwd()+COMMON_PATH +".xml"         #STR
CSV_FILE_PATH = os.getcwd()+COMMON_PATH +".csv"
#print(TEXT_FILE_PATH)
#print(JSON_FILE_PATH)
#print(EXCEL_FILE_PATH)
#print(XML_FILE_PATH)



emplist = get_num_emps(10)


def write_data_into_text():
    with open(TEXT_FILE_PATH,'w') as file:
        for emp in emplist:
            empstr = emp.__str__()
            file.writelines(empstr)
            print(emp.empId ,"Written into file..!")
    print(f'{len(emplist)} employees written into file...!')


#write_data_into_text()

from collections import namedtuple
def read_data_from_text():
    with open(TEXT_FILE_PATH,'r') as file:
        allrecords = file.readlines()
        allrecords = [record.strip() for record in allrecords]
        emplist = []
        for record in allrecords:
            ntuple = namedtuple('employee',['empid','empname','empgen','empage','emprole','empsal','empaddress'])
            ans = record.split('\t\t')
            print(ans)
            ntuple = ntuple(ans[0],ans[1],ans[2],ans[3],ans[4],ans[5],ans[6])
            #print(ntuple)
            emplist.append(ntuple)

        return emplist


#nmt = read_data_from_text()
#print(nmt)

class TextServiceImpl(EmpService):  #plain text --> notepad

    def add_employee(self, empinstance: Employee) -> str: #READABILITY
        if type(empinstance) == Employee:
            with open(TEXT_FILE_PATH,'a') as file:
                empstr = empinstance.__str__()
                file.writelines(empstr)
                return 'Emp Information written successfully...!'
        else:
            raise BaseException('Invalid Employee Type..!')


    def edit_employee(self, eid: int, empvalues: dict) -> Employee:
        pass

    def delete_emp(self, eid: int) -> str:      #first of all read entire data from --> file
       pass                                     #list emp of employess -> given id cha employee delete
                                                # file overrite kara --> with a list--> removed employee nasel.

    def get_employee(self, eid: int) -> Employee: #read
        emplist = self.get_all_employees()
        for emp in emplist:
            if emp.empId == eid:
                return emp

    def get_all_employees(self) -> list:
        emplist = []
        with open(TEXT_FILE_PATH,'r') as file:
            alllines = file.readlines()
            alllines = [record.strip()  for record in alllines]
            for record in alllines:
                fields = record.split('\t\t')
                emp= Employee(eid=fields[0],empnm=fields[1],eag=fields[3],egen=fields[2],emsal=fields[5],erole=fields[4],eaddrs=fields[6])
                emplist.append(emp)
        return emplist


class ExcelServiceImpl(EmpService): #row/coln -->strictly excel
    pass


import csv
def write_data_into_csv_format(emplist):
    with open(CSV_FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        for emp in emplist:
            writer.writerow([emp.empId,emp.empName,emp.empGender,emp.empAge,emp.empRole,emp.empSalary,emp.empAddress])
        #writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
        #writer.writerow([2, "Harry Potter", "Harry Potter"])


#emplist = get_num_emps(10)
#write_data_into_csv_format(emplist)

def read_data_from_csv_format():
    emplist = []
    with open(CSV_FILE_PATH, 'r', ) as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            fields = row[0].split(',')
           # print(fields)
            #emp.empId,emp.empName,emp.empGender,emp.empAge,emp.empRole,emp.empSalary,emp.empAddress
            emp = Employee(eid=fields[0], empnm=fields[1], eag=fields[3], egen=fields[2], emsal=fields[5],
                           erole=fields[4], eaddrs=fields[6])
            emplist.append(emp)
   #print(emplist)
    return emplist

#read_data_from_csv_format()

import csv
# wherever --> u have used -->
class CSVServiceImpl(EmpService):   # values with --> delimiter --> can be comma, selicolon
    def add_employee(self, empinstance: Employee) -> str:
        pass

    def edit_employee(self, eid: int, empvalues: dict) -> Employee:
        pass

    def delete_emp(self, eid: int) -> str:
        emplist = read_data_from_csv_format()   # 10 emps
        flag = False
        for emp in emplist:
            if emp.empId == eid:
                emplist.remove(emp)     # 9
                flag=True
                break
        if flag:
            write_data_into_csv_format(emplist) # 9 ch write karel --> kind of delete operation
            print('Employee record removed...')
        else:
            print('No employee with given id..')

    def get_employee(self, eid: int) -> Employee:
        pass

    def get_all_employees(self) -> list:
        pass
        # can be opened inside notepad + excel


emplist = get_num_emps(10)  # emplist -->

import json
def write_datainto_json():
        empdictinfo = []            # emps --dicts
        for emp in emplist:     # one by one --
            empdictinfo.append(emp.__dict__)        # emp -> dict       -- key:value -->json

        ans = json.dumps(empdictinfo)       # dump --> json - tayar kela
        with open(JSON_FILE_PATH, 'w') as file:
            file.writelines(ans)        # write kela --> file madhe

#write_datainto_json()

def read_data_from_json():
    with open(JSON_FILE_PATH,'r') as file:
        jsoncontents = json.load(file)      #jsoncontents --> [{},{},{}]
        print(jsoncontents[5].get('empName'))       #get

read_data_from_json()


class JsonServiceImpl(EmpService):  #json --> kind of dict--> key:value
    pass


class DatabaseServiceImpl(EmpService):
    pass


if __name__ == '__main__':
    #textService = TextServiceImpl()
    ##emplist = textService.get_all_employees()
    #print(emplist)
    #csvService = CSVServiceImpl()
    #csvService.delete_emp(115)
    import sys
    sys.exit(0)
    textService.add_employee(get_num_emps(1)[0])
    textService.add_employee(get_num_emps(2)[0])
    textService.add_employee(get_num_emps(3)[0])
    textService.add_employee(get_num_emps(4)[0])

#SQL -->
    #https://dev.mysql.com/downloads/installer/  -->
    #https://www.postgresql.org/download/windows/

#https://www.tutorialspoint.com/json/index.htm


#FLASK --> ORM --> DATABASE -->< FLASK MADHE-->


#textservice/jsonservice/csvservice --> read[single/all]/write/update/delete --> crud operations-->

'''
  #file  = open('')    # we need to explicitly close the file ->resources
    with open('') as file:      # context manager --> with block execution complete  hoel -> automatically file will be closed
        pass

'''