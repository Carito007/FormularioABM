import re
from datetime import datetime

def emailValidator(email):

  if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
    return True
  else:
    return False
def dateValidator(nacimiento):
  try:
    datetime.strptime(nacimiento,'%d/%m/%Y')
    return True
  except:
    return False
def nameValidator(username):
  if re.match(r'^[a-zA-Z\s]+$',username) and len(username)>=3:
    return True
  else:
    return False
  
