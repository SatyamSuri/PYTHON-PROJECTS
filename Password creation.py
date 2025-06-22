import random
import string

pass_len = int(input("enter the length of password : "))
charVal = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(pass_len):
    password += random.choice(charVal)

print("your random password is : ", password)
