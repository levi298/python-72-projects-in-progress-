import random 

l = int(input("lenghth of the password: "))

characters = "abcdef4gh5ij6kl7mno8pq9rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&123"
password=""

for i in range (l):
    password=password+random.choice(characters)

print(password)