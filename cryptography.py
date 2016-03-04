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
quit = False

while quit == False:
    i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if i not in('e','d','q'):
        print("Did not understand command, try again.")
        i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if i=="e":
        message=input("Message: ")
        key=input("Key: ")
        m=len(message)
        k=len(key)
        if m>k:
            count = key * ((m-(m%k))/k)
            trun = key[0:(m%k)]
            newkey = count + trun
            print(newkey, message)
        for x in (0,m-1):
            let.append(associations.find(message[x]))
        for y in range (0,k-1):
            kelt.append(associations.find(message[y]))
        q=m-k
        kelt.append(associations.find(message[1]))
        print(kelt)
    if i=="d":
        
        print(let)
    if i=="q":
        print("Goodbye!")
        quit = True
        
        
