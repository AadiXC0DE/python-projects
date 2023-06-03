#Generating random passwords
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


#function to generate password
def generate_password():
    password_length=int(input("Enter the length of password:"))
    random.shuffle(characters)
    password=[]

    for i in range (password_length):
        password.append(random.choice(characters))

    random.shuffle(password)   
    password = "".join(password)
    print(password)

choice=input("do you want to generate a password ? (Yes/No):")
if choice=="Yes":
    generate_password()
elif choice =="No":
    print("Ended")
    quit()
else:
    print("Invalid input")
    quit()            