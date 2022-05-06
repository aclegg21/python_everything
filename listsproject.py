#Creates blank list
This_list = [] 

#Prints blank list
print(This_list) 

#Prints blank list
This_list.append("S3") 

#Adds 'Lambda' to list
This_list.append("Lambda") 

#Adds 'EC2' to list
This_list.append("EC2") 

#Prints list with 3 items on it
print(This_list) 

#Tells me how big list is
print (len(This_list)) 

#Deletes 'Lambda' from list
del This_list[1] 

#Deletes 'S3' from list
del This_list[0] 

#Prints new list with two less items on it
print(This_list) 

#Tells me how big new list is
print (len(This_list))
