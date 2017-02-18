input_string = raw_input("Enter your text to cypher : ")
input_key = int(raw_input("Enter the number to be used to cypher : "))

secret_string = ""
temp_char = None


for char in input_string:
    char_code = 0
    if char.isdigit() or char.isspace():
        secret_string = secret_string + char
    elif char.isalpha():
        if char.isupper():
            char_code = ord(char)
            char_code = char_code + input_key
            if char_code > ord('Z'):
                char_code = char_code - 26
            elif char_code < ord('A'):
                char_code = char_code + 26
        elif char.islower():
            char_code = ord(char)
            char_code = char_code + input_key
            if char_code > ord('z'):
                char_code = char_code - 26
            elif char_code < ord('a'):
                char_code = char_code + 26

        secret_string = secret_string + chr(char_code)
    else:
        secret_string = secret_string + char

print "The Secret Message converted is : " , secret_string

input_key = -input_key
decrypt_message = ""
for char in secret_string:
    char_code = 0
    if char.isdigit() or char.isspace():
        decrypt_message = decrypt_message + char
    elif char.isalpha():
        if char.isupper():
            char_code = ord(char)
            char_code = char_code + input_key
            if char_code > ord('Z'):
                char_code = char_code - 26
            elif char_code < ord('A'):
                char_code = char_code + 26
        elif char.islower():
            char_code = ord(char)
            char_code = char_code + input_key
            if char_code > ord('z'):
                char_code = char_code - 26
            elif char_code < ord('a'):
                char_code = char_code + 26

        decrypt_message = decrypt_message + chr(char_code)
    else:
        decrypt_message = decrypt_message + char

print "Decrypted Back to Normal : " , decrypt_message
