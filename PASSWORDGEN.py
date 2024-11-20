print("\033[2J\033[H", end="")
print("""\

# ················································································
# :                                                                              :
# :                                                                              :
# :    ____       _      ____       ____   __        __   ___    ____    ____    :
# :   |  _ \     / \    / ___|     / ___|  \ \      / /  / _ \  |  _ \  |  _ \   :
# :   | |_) |   / _ \   \___ \     \___ \   \ \ /\ / /  | | | | | |_) | | | | |  :
# :   |  __/   / ___ \   ___) |     ___) |   \ V  V /   | |_| | |  _ <  | |_| |  :
# :   |_|___  /_/___\_\_|____/ ____|____/__   \_/\_/     \___/  |_|_\_\ |____/   :
# :    / ___| | ____| | \ | | | ____| |  _ \     / \    |_   _|  / _ \  |  _ \   :
# :   | |  _  |  _|   |  \| | |  _|   | |_) |   / _ \     | |   | | | | | |_) |  :
# :   | |_| | | |___  | |\  | | |___  |  _ <   / ___ \    | |   | |_| | |  _ <   :
# :    \____| |_____| |_| \_| |_____| |_| \_\ /_/   \_\   |_|    \___/  |_| \_\  :
# :                                                                              :
# :                                                                              :
# :                                                                              :
# ················································································

""")
text = (
        "\n***************************************************\t\n"
        "\n\033[38:5:25mPASSWORD GENERATOR USING PYTHON\033[0m\n"
        "\n***************************************************\n")

print("{:.^100}".format(text))


print("\033[2J\033[H", end="")

import string
import random
#Ask user for password strength
print('''\nSelect the type of password you want:
1. Weak    (Only lowercase letters)
2. Okay    (Lowercase, uppercase letters, and digits)
3. Strong  (Letters, digits, special characters)
4. Custom  (You choose character set)
''')

strength_choice = int(input("\033[38;2;255;0;255mEnter your choice (1,2,3,4).....: \033[0m"))

length = int(input("\033[38;2;255;0;255mEnter the desired length of the password.....: \033[0m"))

characterList = ""

if strength_choice == 1:
    
    characterList = string.ascii_lowercase
    print("\033[32mYou selected a Weak password.\033[0m")
elif strength_choice == 2:

    characterList = string.ascii_letters + string.digits
    print("\033[32mYou selected an Okay password.\033[0m")
elif strength_choice == 3:
    
    characterList = string.ascii_letters + string.digits + string.punctuation
    print("\033[32mYou selected a Strong password.\033[0m")
elif strength_choice == 4:
    print("\033[2J\033[H", end="")
    
    #print("\033[2J\033[H", end="")
    text = (
        "\n***************************************************\t\n"
        "\n\033[38:5:25mPASSWORD GENERATOR USING PYTHON\033[0m\n"
        "\n***************************************************\n")

    print("{:.^100}".format(text))
    print("\033[32mYou selected customised password.\033[0m")

    print('''Choose the character set you want to use in your password:
1. Letters
2. Digits
3. Special characters
4. Exit
''')
    while True:
        choice = int(input("Enter your choice.......: "))
        if choice == 1:
            characterList += string.ascii_letters
            print("\033[32mLetters added to your character set!\033[0m")
        elif choice == 2:
            characterList += string.digits
            print("\033[32mDigits added to your character set!\033[0m")
        elif choice == 3:
            characterList += string.punctuation
            print("\033[32mSpecial characters added to your character set!\033[0m")
        elif choice == 4:
            if not characterList:
                print("\033[31mYou must select at least one character set before exiting!\033[0m")
            else:
                break
        else:
            print("\033[31mPlease enter a valid number! (1-4)\033[0m")
else:
    print("\033[31mInvalid choice! Please restart the program and select a valid option.\033[0m")
    exit()

# Generate password
password = "".join(random.choice(characterList) for _ in range(length))

print("\033[2J\033[H", end="")



text = (
        "\n***************************************************\t\n"
        "\n\033[38:5:25mPASSWORD GENERATOR USING PYTHON\033[0m\n"
        "\n***************************************************\n")

print("{:.^100}".format(text))

#
# Display the generated password
print("\033[31mYour new generated password is:\033[1m" + password + "\033[0m")

print("\033[38:5:25mTHANK YOU\033[0m")




