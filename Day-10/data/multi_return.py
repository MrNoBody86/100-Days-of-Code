#Multiple return values 

def format_name(f_name,l_name):
  if f_name == "" or l_name =="":
    return "You didn't provide valid inputs"
  F_name = f_name.title()
  L_name = l_name.title()
  return f"Result :{F_name} {L_name}"

print(format_name(input("What is your first name? "),input("What is your last name? ")))