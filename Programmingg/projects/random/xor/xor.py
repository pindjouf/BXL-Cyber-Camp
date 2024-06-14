def encrypt(plaintext, secret_key):
    plaintext = int(input("Enter the plaintext: "))
    secret_key = int(input("Enter the secret key: "))
    return ciphertext

encrypt()

ciphertext = []

# Compare the bits
for x,y in zip(plaintext, secret_key):
    if x == y:
        ciphertext.append(0)
    else:
        ciphertext.append(1)

# Convert bit to decimal
deci_ciphertext = int(''.join(map(str, ciphertext)), 2)

print("The ciphertext is: {}".format(ciphertext))
print("Decimal value: {}".format(deci_ciphertext))
