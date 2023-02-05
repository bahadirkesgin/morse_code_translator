import random
import string
import time

morse_code_dict = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def search_with_values(dict, value):
    key = str([k for k, v in dict.items() if v == value])
    try:
        key = key[2]
    except IndexError:
        key = " "
    return key

def print_decrypted_text(decrypted_text, fancy_print = True):
    if fancy_print:
        list_items = string.ascii_letters + " -+?,0123456789./()"
        txt_wri = decrypted_text + " "
        i = 0
        new_txt = ""
        count = 0

        while i in range(0, len(txt_wri)):
            a = random.choice(list_items)
            if new_txt.__contains__(decrypted_text):
                print("\r", new_txt)
                print("Number of steps: " + str(count))
                break
            elif a == txt_wri[i]:
                new_txt = new_txt + txt_wri[i]
                time.sleep(0.01)
                i = i + 1
                count = count + 1
            else:
                if i > 0:
                    print("\r", new_txt + a, end="")
                    time.sleep(0.004)
                    count = count + 1
                else:
                    print("\r", a, end="")
                    time.sleep(0.006)
                    count = count + 1
        f = open("decrypted_text.mtt", "w")
        f.write(decrypted_text)
        f.close()
    else:
        f = open("decrypted_text.mtt", "w")
        f.write(decrypted_text)
        f.close()
        print(decrypted_text)

def print_encrypted_text(encrypted_text, fancy_print = True):
    if fancy_print:
        list_items = ".- "
        txt_wri = encrypted_text + " "
        i = 0
        new_txt = ""
        count = 0
        while i in range(0, len(txt_wri)):
            a = random.choice(list_items)
            if new_txt.__contains__(encrypted_text):
                print("\r", new_txt)
                print("Number of steps: " + str(count))
                break
            elif a == txt_wri[i]:
                new_txt = new_txt + txt_wri[i]
                time.sleep(0.01)
                i = i + 1
                count = count + 1
            else:
                if i > 0:
                    print("\r", new_txt + a, end="")
                    time.sleep(0.004)
                    count = count + 1
                else:
                    print("\r", a, end="")
                    time.sleep(0.006)
                    count = count + 1
        f = open("encrypted_text.mtt", "w")
        f.write(encrypted_text)
        f.close()
    else:
        print(encrypted_text)
        f = open("encrypted_text.mtt", "w")
        f.write(encrypted_text)
        f.close()

def encrypt(user_inp):
    fancy_inp = input("Do you want to print the encrypted text in a fancy way? (y/n): ").lower()
    if fancy_inp == "y":
        fancy_print = True
    else:
        fancy_print = False
    user_inp = user_inp.upper()
    user_input = user_inp + ""
    encrypted_text = ""
    i = 0
    while i in range(0, len(user_input)):
        if user_input[i] != " ":
            encrypted_text = encrypted_text + morse_code_dict[user_input[i]] + " "
            i = i + 1
        else:
            encrypted_text = encrypted_text + "  "
            i = i + 1
    print_encrypted_text(encrypted_text, fancy_print)

def decrypt(user_inp):
    fancy_inp = input("Do you want to print the decrypted text in a fancy way? (y/n): ").lower()
    if fancy_inp == "y":
        fancy_print = True
    else:
        fancy_print = False
    decrypted_text = ""
    morse_batch = ""
    user_inp = user_inp.upper()
    user_input = user_inp + " "
    i = 0
    while i in range(0, len(user_input)):
        if user_input[i] != " ":
            morse_batch += user_input[i]
            i = i + 1
        elif user_input[i] == "  ":
            decrypted_text += " "
            i = i + 1
        else:
            decrypted_text = decrypted_text + search_with_values(morse_code_dict, morse_batch)
            morse_batch = ""
            i = i + 1
    print_decrypted_text(decrypted_text, fancy_print)

def main():
    print("Welcome to the Morse Code Translator!")
    print("1. Encrypt a text")
    print("2. Decrypt a text")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        user_inp = input("Enter the text to encrypt: ")
        encrypt(user_inp)
        another_inp = input("Do you want to do another translation (y/n): ").lower()
        if another_inp == "y":
            main()
        else:
            exit()
    elif choice == "2":
        user_inp = input("Enter the text to decrypt: ")
        decrypt(user_inp)
        another_inp = input("Do you want to do another translation (y/n): ").lower()
        if another_inp == "y":
            main()
        else:
            exit()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice!")
        main()

main()