import re

regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' # Any custom email id possible. Must contain '@' and "." 
regex_name = '[A-Za-z]{2,25}' #\s[A-Za-z]{2,25}  Add for space between names
regex_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&.])[A-Za-z\d@$!#%*?&.]{4,20}$'

def check_mail(email):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex_email,email)):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email")

def check_name(name):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex_name,name)):  
        print("Valid Name")  
          
    else:  
        print("Invalid Name")

def check_pass(password):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex_password,password)):  
        print("Valid Password")  
          
    else:  
        print("Invalid Password")

if __name__ == '__main__' :  
      
    # Enter the details 
    name = "rushial" 
    email = "ankitrai326@gmail.com" 
    password = "Rush22"
      
    # calling run function  
    check_mail(email) 
    check_name(name) 
    check_pass(password) 