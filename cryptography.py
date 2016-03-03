"""
cryptography.py
Author: Payton
Credit: Avery, Daniel

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
let=[]
kelt=[]

i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if i not in('e','d','q'):
    print("Did not understand command, try again.")
    i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if i=="e":
    message=input("Message: ")
    key=str(input("Key: "))
    m=len(message)
    k=len(key)
    for x in (0,m):
        let.append(associations.find(message[x]))
    for y in range (0,k):
        kelt.append(associations.find(message[y]))
    q=l-k
    kelt.append(associations.find(message[-q]))
    print(message)
if i=="d":
    print(let)
if i=="q":
    print("Goodbye!")