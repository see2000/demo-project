#print(x)
"""try:
    print(x)
except:
    print("an errors is there")"""
'''try:
    print(x)
except NameError:
    print("variable is not defined")
except:
    print("an error is there")'''
try:
    print("x")
except:
    print("an error occured")
else:
    print("there is no errors")
finally:
    print("the program is completed")
x=int(input("enter any number"))
if x<0:
    raise Exception("negative numbers are not allowed")
