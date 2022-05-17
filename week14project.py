import uuid
def namegenerator():
    number_of_names = int(input("How many names do you need? "))
    name_department = input("What is the name of your department? Please use Marketing, Accounting, or FinOps: ")
    uppername = name_department.upper()
    counter = 0
    
    
    if uppername != "MARKETING" and uppername != "ACCOUNTING" and uppername != "FINOPS":
        print("Do not use this name generator")
        exit()
        
    while counter < number_of_names:
        print(str(uuid.uuid4()) + name_department)
        
        counter += 1
        
        
namegenerator()