import random

def SecretSantaList():
    output = {}        
    f = open("employee.txt", "r") 
    employees = f.read().split("\n")
    f.close()
    if len(employees) <= 1:
        print("Not Enough Employees")
    else:          
        random.shuffle(employees)
        f = open("output.txt","w")
        f.write('{0:10}  {1:14}\n\n'.format("EMPLOYEE","SECRET SANTA"))
        for i in range(len(employees)):
            output[employees[i]] = employees[(i%len(employees)+1)%len(employees)]
            santa = '{0:10}  {1:14}\n'.format(employees[i],output[employees[i]])
            f.write(santa) 
        f.close()         
        # print(output) You can print output on terminal

SecretSantaList()