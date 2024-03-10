import sheety

print("Welcome to Aryan's Flight Club. \nWe find the best flight deals and email you. ")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email = "email1"
email_confirm = "email2"

while email != email_confirm:
    email = input("What is your email? ")
    if email.lower() == "quit" \
              or email.lower() == "exit":
        exit()
    email_confirm = input("Please verify your email : ")
    if email_confirm.lower() == "quit" \
              or email_confirm.lower() == "exit":
        exit()

print("OK. You're in the club!")

sheety.post_new_row(first_name, last_name, email)
