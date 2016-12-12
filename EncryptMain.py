# Can encrypt or decrypt messages given a message, key, and method
import math


# Asks if encrypting or decrypting
def main():
    whatDo = input("What would you like to do?").lower()
    if whatDo == "encrypt":
        encrypt()
        again()
    elif whatDo == "decrypt":
        decrypt()
        again()
    else:
        print("Please enter Encrypt or Decrypt.")
        main()


# Runs proper function given message, key type, key, and encryption method
def encrypt():
    while True:
        mode = input("Is your key numeric or alphabetical?").lower()
        if mode == "numeric":
            key = int(input("Your key must be a positive integer and not be 1. What is your key?"))
            while key <= 1:
                key = int(input("Your key cannot be 0, 1, or a negative value, please enter a valid key"))
            break
        elif mode == "alphabetical":
            key = str(input("Your key must not contain any symbols or numbers. What is your key?"))
            break
        else:
            print("That is not an available key format.")
    msg = str(input("What is your message?"))
    # This gives available encryption methods given the type of key
    print("Which encryption method would you like to use?")
    if mode == "numeric":
        while True:
            method = input("You can use these encryption methods: Simple Caesar Cipher and Transposition, please choose one.").lower()
            if method == "transposition":
                encryptTranspo1(msg, key)
                break
            elif method == "simple caesar cipher":
                method = "e"
                Caesar1(msg, key, mode, method)
                break
            else:
                print("That is not an available method for encryption, please enter a correct method.")
    elif mode == "alphabetical":
        while True:
            method = input("You can use these encryption methods: Simple Caesar Cipher, please choose one.").lower()
            if method == "simple caesar cipher":
                typeofKey = 0
                Caesar1(msg, key, typeofKey, mode)
                break
            elif method == "placeholder2":
                # encrypt.placeholder2(msg,key)
                break
            else:
                print("That is not an available method for encryption, please enter a correct method.")


# Runs proper function based on message, key type, key, and encryption method.
def decrypt():
    while True:
        typeOfKey = input("What type of key was used?")
        if typeOfKey == "numeric":
            key = int(input("What is the key?").lower())
            break
        elif typeOfKey == "alphabetical":
            key = input("What is the key?").lower()
            break
        else:
            print("Please enter either \"Numeric\" or \"Alphabetical.\"")
    msg = input("What is the encrypted message?")
    while True:
        method = input("What method of encryption was used?")
        if method == "transposition":
            decryptTranspo1(msg, key)
            break
        elif method == "simple caesar cipher":
            mode = "d"
            Caesar1(msg, key, typeOfKey, mode)
            break
        else:
            print("That is not an available method for decryption, please enter a correct method.")


# asks if user wants to do it again
def again():
    cont = input("Would you like to encrypt or decrypt another string?").lower()
    if cont == "yes":
        main()
    elif cont == "no":
        print("Program ended.")
    else:
        print("Thar is an invalid answer, please type yes or no.")
        again()


# encrypts using transposition)
def encryptTranspo1(message, key):
    encryptArr = [''] * key
    for x in range(key):
        select = x
        while select < len(message):
            encryptArr[x] += message[select]
            select += key
    encrypted = ''.join(encryptArr)
    print("Your key is", key, "and your encrypted string is \""+ encrypted +"|\"")


# decrypts using transposition
def decryptTranspo1(message, key):
    numCol = math.ceil(len(message)/key)
    numRow = key
    numUnused = (numCol * numRow) - len(message)
    encryptArr = [''] * numCol
    col = 0
    row = 0
    for place in message:
        encryptArr[col] += place
        col += 1
        if (col == numCol) or (col == numCol - 1 and row >= numRow - numUnused):
            col = 0
            row += 1
    decrypted = ''.join(encryptArr)
    print(decrypted)


def Caesar1(message, key1, method, mode):
    # for every character in message, translate and add to new string
    if method == "alphabetical":
        key = 0
        for char in key1:
            key += ord(char)
    else:
        key = key1
    while key >= 26:
        key -= 26
    if mode == "d":
        key *= -1
    else:
        key = key
    encryptedString = ""
    for character in message:
        if character.isalpha():
            charNum = ord(character) + key
            if character.isupper():
                if charNum > 90:
                    charNum -= 26
                elif charNum < 65:
                    charNum += 26
                else:
                    charNum = charNum
            elif character.islower():
                if charNum > 122:
                    charNum -= 26
                elif charNum < 97:
                    charNum += 26
                else:
                    charNum = charNum
            else:
                print("This shouldnt happen")
            encryptedString += chr(charNum)
        else:
            encryptedString += character
    print("Your key is", key1, "and your encrypted string is \"" + encryptedString + "\"")

# Begins the program
main()