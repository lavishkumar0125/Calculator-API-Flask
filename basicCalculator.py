def basic_calculator(a,b,operation):
    if(a.isnumeric() & b.isnumeric()):
        a = int(a)
        b = int(b)
        if(operation == "+"):
            result = a+b
        elif(operation == "-"):
            result = a-b
        elif(operation == "*"):
            result = a*b
        elif(operation == "/"):
            result = a/b 
        else:
            result = "UnSupported Operation"
    else:
        result = "Please enter a valid number for a & b"
    return result;                   