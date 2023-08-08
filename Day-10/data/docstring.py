#Docstring

#Multiple return values 

def format_name(f_name,l_name):
  """This function takes first name and last name as input and convert them to a title and returns the full name"""
  if f_name == "" or l_name =="":
    return "You didn't provide valid inputs"
  F_name = f_name.title()
  L_name = l_name.title()
  return f"Result :{F_name} {L_name}"

format_name()
