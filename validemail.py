import re
def check(a):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

 
    if(re.fullmatch(regex, a)):
        print("Valid Email")
 
    else:
        print("Invalid Email")

a="ryan@gmail.com";
check(a);
        
