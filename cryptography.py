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
    m=len(message)
    k=len(key)
    for x in (0,m):
        let.append(associations.find(message[x]))
    while k<1:
        a=len(let)
        k=len(key)
        if k<1:
            for y in range (0,k):
                
    print(message)
if i=="d":
    print(key)
    print(message)
    print(message)
if i=="q":
    print("Goodbye!")
elif not i=="e" or i =="d" or i=="q":
    print("Did not understand command, try again.")