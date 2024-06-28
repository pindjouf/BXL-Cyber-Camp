import os

# Get user input
text = input("Gimme some input: ")
key = input("Gimme a key: ")

# Define the values
plaintext = []
secret_key = []
ciphertext = []

# Put user input in list
for i in text:
    plaintext.append(int(i))

for i in key:
    secret_key.append(int(i))

# Make list length equal for operation
if len(plaintext) < len(secret_key):
    result = len(secret_key) - len(plaintext)
    for i in range(result):
        plaintext.insert(0, 0)

elif len(secret_key) < len(plaintext):
    result = len(plaintext) - len(secret_key)
    for i in range(result):
        secret_key.insert(0, 0)

print(plaintext)
print(secret_key)

# Get ciphertext from XOR operation
for x,y in zip(plaintext, secret_key):
    if x == y:
        ciphertext.append(0)
    else:
        ciphertext.append(1)

# Make ciphertext pretty
pretty_ci = ''.join(map(str, ciphertext))

# Convert bits to decimal
deci_ciphertext = int(''.join(map(str, ciphertext)), 2)

# Clear screen pre-print
# os.system('clear')

print("The ciphertext is: {}".format(pretty_ci))
print("Decimal value: {}".format(deci_ciphertext))
