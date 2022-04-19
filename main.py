def valid_int(lb,ub,prompt,error):
  not_valid=True
  while not_valid:
    try:
      int_value=int(input(prompt))
      if int_value not in range(lb,ub +1):
          raise ValueError
      not_valid=False
    except ValueError:
          print(f"\033[31m{error}\033[0m")
    return int_value

def encrypt(key, txt):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    caesar={}
    for index, letter in enumerate(alphabet):
        caesar[letter]=alphabet[(index+key) % len(alphabet)]

    print(caesar, "\n")

    encrypted=""
    
    for letter in txt:
      try:
        encrypted +=caesar[letter]
      except KeyError:
        encrypted += letter
      
    return encrypted


#encrypt

#1.encrypt key between 1 & 25
key=valid_int(1,25,"choose an encryption key\n>>> ", "Encryption keys must be between 1 and 25")

#2. text users wishes to encrypt
text=input("enter the key you wish to encrypt\n>>>").lower()

#3. encrypt user's text
encrypted=encrypt(key, text)

#4. display encrypted text
print(f"your encrypted text is: \n\033[32m{encrypted}\033[0m\n")







"""
Aaron answer:

# CAESAR CIPHER


def valid_int(lb, ub, prompt, error):
    not_valid = True
    while not_valid:
        try:
            int_value = int(input(prompt))
            if int_value not in range(lb, ub + 1):
                raise ValueError
            not_valid = False
        except ValueError:
            print(f"\033[31m{error}\033[0m")
    return int_value


def encrypt(key, txt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    caesar = {}
    for index, letter in enumerate(alphabet):
        caesar[letter] = alphabet[(index + key) % len(alphabet)]

    print(caesar, "\n")

    encrypted = ""
    for letter in txt:
        try:
            encrypted += caesar[letter]
        except KeyError:
            encrypted += letter

    return encrypted


# ENCRYPT

# 1. Ask the user for an encryption key between 1 & 25
key = valid_int(1, 25, "Choose an encryption key\n>>> ",
                "Encryption keys must be integers between 1 & 25")

print(f"\nYour encryption key is:\n\033[32m{key}\033[0m\n")

# 2. Ask the user for the text they wish to encrypt
text = input("Enter the text you wish to encrypt\n>>> ").lower()

print(f"\nYour text is:\n\033[32m{text}\033[0m\n")

# 3. Encrypt the user's text
encryted = encrypt(key, text)

# 4. Display the encrypted text
print(f"Your encryted text is:\n\033[32m{encryted}\033[0m\n")


# DECRYPT
# "dkalj djhak" -> "hello world"

"""