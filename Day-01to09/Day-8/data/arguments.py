#Positinal vs Keyword Argument

#Functions with more than 1 input

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")
greet_with("Mr.nobody","Nowhere")#positional argument

greet_with(location="thenthere",name = "Mrs.everybody")#Keyword argument