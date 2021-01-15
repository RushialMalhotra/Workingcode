import re

regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' # Any custom email id possible. Must contain '@' and "." 
regex_name = '[A-Za-z]{2,25}' #\s[A-Za-z]{2,25}  Add for space between names
regex_password = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,}$'

def check_mail(email):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex_email,email)):  
        return True 
          
    else:  
        return False

def check_name(name):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex_name,name)):  
        return True
          
    else:  
        return False

def check_pass(password):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex_password,password)):
        return True 
          
    else:  
        return False
      