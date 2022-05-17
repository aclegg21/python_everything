value = int(input("Please enter a score: "))

if value > 0 and value < 60:     #Value is greater than 0 and less than 60 to return F
    print("F")
elif value >= 60 and value < 70: #Value is greater than or equal to 60 and less than 70 to return D
    print("D")
elif value >= 70 and value < 80: #Value is greater than or equal to 70 and less than 80 to return C
    print("C")
elif value >= 80 and value < 90: #Value is greater than or equal to 80 and less than 90 to return B
    print("B")
elif value >= 90: #Value is greater than or equal to 90 return A
    print("A")
else:
    print("Go study harder!") #If less than 0 return this message