from abc import ABC,abstractmethod

from file_handling_persist_ops.employeeinfo import Employee
class EmpService(ABC):

    @abstractmethod
    def add_employee(self,empinstance:Employee)->str:
        pass

    @abstractmethod
    def edit_employee(self,eid:int,empvalues:dict)->Employee:
        pass

    @abstractmethod
    def delete_emp(self,eid:int)->str:
        pass

    @abstractmethod
    def get_employee(self,eid:int)->Employee:
        pass

    @abstractmethod
    def get_all_employees(self)->list:
        pass

