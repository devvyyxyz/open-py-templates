import random

print("Password generator by Devvyyxyz")


chars='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!£$%&^*@?'
length = input("How long would you like your password to be?")
length = int(length)

password = ''
for c in range(length):
  password += random.choice(chars)

print(password)
print("Write this down somewhere safe or store in a password manager!")
