from ceaser_data import logo
from ceaser_data import alphabet

print(logo)


def ceaser(start_text, shift_amount, cipher_direction):
    end_result = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for character in start_text:
        if character in alphabet:
            position = alphabet.index(character)
            new_pos = position+shift_amount
            end_result += alphabet[new_pos]
        else:
            end_result += character
    print(f"The {cipher_direction}d text is {end_result}")


# def encrypt(msg, shiftNumber):
#     result = ""
#     for character in msg:
#         index = alphabet.index(letter)
#         result = result+alphabet[index+shiftNumber]

#     print(f"Your Encoded msg is {result}")


# def decrypt(msg, shiftNumber):
#     result = ""
#     for letter in msg:
#         index = alphabet.index(letter)
#         result = result+alphabet[index-shiftNumber]
#     print(f"Your Decoded msg is {result}")


# if(action == 'encode'):
#     encrypt(msg=message, shiftNumber=shift)
# elif(action == 'decode'):
#     decrypt(msg=message, shiftNumber=shift)
# else:
#     print("Wrong Input,Try Again!")

should_continue = True
while should_continue:
    action = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")

    message = input("Type your Message!\n").lower()
    shift = int(input("Enter the shift number:\n"))

    shift = shift % 26
    ceaser(start_text=message, shift_amount=shift, cipher_direction=action)
    result = input(
        "Type 'Y' if you want to go again.Otherwise type 'N'\n").lower()
    if result == "n":
        should_continue = False
        print("Goodbye")
