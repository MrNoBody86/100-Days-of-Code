import requests

URL = "https://api.sheety.co/407bd5b3fc8ff807ff0ce54e08b178fd/flightDeals/users"

print("Welcome to Aryan's Flight Club. \nWe find the best flight deals and email you. ")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")
email_confirm = input("Type your email again. ")
if email == email_confirm:
  print("You're in the club!")
else :
  print("Emails do not match. Please try again.")

new_data = {
  "user" : {
    "firstName" : first_name,
    "lastName" : last_name,
    "email" : email
  }
}

response = requests.post(url=URL, json=new_data,timeout=None)

print(response.text)

