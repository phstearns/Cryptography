"""
cryptography.py
Author: Payton
Credit: Avery, Daniel

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if i=="e":
    message=input("Message: ")
    key=str(input("Key: "))
    l=len(message)
    print(message)
if i=="d":
    print(message)
    print(key)
    print(message)
if i=="q":
    print("Goodbye!")
elif not i=="e" or i =="d" or i=="q":
    print("Did not understand command, try again.")