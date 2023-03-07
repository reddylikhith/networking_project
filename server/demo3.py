import pandas as pd
from openpyxl.workbook import Workbook
class Employee:
    def _init_(self,name,sap,address,contact):
        self.name=name
        self.sap=sap
        self.address=address
        self.contact=contact

    def get_details(self):
        return f"Name: {self.name}\nsap: {self.sap}\naddress: {self.address}\ncontact: {self.contact}"
employee_list = [
Employee("Manjusha", "52138223", "hcl Chennai", "12345678"),
Employee("Jafar", "52138728", "hcl Chennai", "123456789"),
Employee("Phani", "52138723", "hcl Chennai", "12345678"),
Employee("Bhagya", "52138724", "hcl Chennai", "123456578"),
Employee("Nabela", "52138710", "hcl pune", "12345678"),
Employee("Sulochana", "52140930", "hcl Chennai", "123456678"),
Employee("Lakshmi", "52138220", "hcl banglore", "12345678"),
Employee("Sindhu", "52138700", "hcl Chennai", "123456748"),
Employee("Test", "0000001", "hcl test", "000000001"),

]
df1 = pd.DataFrame(data=[(e.name,e.sap,e.address,e.contact) for e in employee_list],columns=["Name", "sap", "address", "contact"])
#print(df1)
"""for Employee in employee_list:
    print(Employee.get_details(), "\n")"""
class Project:
    def _init_(self,Project_ID,sap,Project_Name):
        self.Project_ID=Project_ID
        self.sap=sap
        self.Project_Name=Project_Name


    def get_details(self):
        return f"Project_ID: {self.Project_ID}\nsap: {self.sap}\nProject_Name: {self.Project_Name}"



project_list = [
Project("0001", "52138929", "Cisco"),
Project("0002", "52138223", "Intel"),
Project("0003", "52138728", "Hcl"),
Project("0004", "52138723", "Infosys"),
Project("0005", "52138724", "Tcs"),
Project("0005", "52138710", "Wipro"),
Project("0006", "52140930", "Nike"),
Project("0007", "52138220", "Deloitee"),
Project("0008", "52138700", "Info Tech"),
Project("0009", "0000001", "Hcl Test"),

]

"""for project in project_list:
    print(project.get_details(), "\n")"""
df2 = pd.DataFrame(data=[(e.Project_ID,e.sap,e.Project_Name) for e in project_list],columns=["Id", "sap", "Project_Name"])
#print(df2)
inner=pd.merge(df1,df2,on="sap")
print(inner)
inner.to_excel('data_file.xlsx')
#Workbook.close()