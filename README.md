### README

# Password Generator using Python

---

## **Introduction**
This Python script is a simple yet powerful password generator that creates random passwords based on user-defined preferences. It allows users to customize the strength and character set of the password to meet their security needs.

---

## **Features**
- **Password Strength Levels**:
  - **Weak**: Contains only lowercase letters.
  - **Okay**: Includes lowercase, uppercase letters, and digits.
  - **Strong**: Includes letters, digits, and special characters.
  - **Custom**: Allows users to select their own character set.
  
- **Interactive User Interface**:
  - Users can choose the type and length of the password.
  - For the custom option, users can add letters, digits, and special characters to their character set interactively.

- **Dynamic Display**:
  - The program uses terminal commands to clear the screen and create a clean, organized user interface.





## **How to Use**
1. **Select Password Strength**:  
   Upon running the script, you will be prompted to choose from one of the following options:
   - Weak (Option 1)
   - Okay (Option 2)
   - Strong (Option 3)
   - Custom (Option 4)

2. **Specify Password Length**:  
   Enter the desired length of your password.

3. **(Custom Option Only)** Choose Character Sets:  
   - Add letters, digits, or special characters to your custom character set.
   - You must select at least one character set before exiting.

4. **View Generated Password**:  
   The script will display your new randomly generated password.

---

## **Code Overview**

### **Modules Used**
- `string`: Provides predefined sets of characters like letters, digits, and punctuation.
- `random`: Used to generate random selections from the chosen character set.

### **Key Sections**
1. **Password Strength Selection**:
   - Determines the character set based on user input.
   
2. **Custom Character Set**:
   - Allows users to build their own character set interactively.

3. **Password Generation**:
   - Creates a password by randomly selecting characters from the defined character set.

4. **Display and UI**:
   - Uses escape sequences (`\033`) to create a dynamic and colorful interface.

---

## **Sample Output**

```
***************************************************

   PASSWORD GENERATOR USING PYTHON

***************************************************

Select the type of password you want:
1. Weak    (Only lowercase letters)
2. Okay    (Lowercase, uppercase letters, and digits)
3. Strong  (Letters, digits, special characters)
4. Custom  (You choose character set)

Enter your choice (1,2,3,4).....: 3
Enter the desired length of the password.....: 12

***************************************************

   PASSWORD GENERATOR USING PYTHON

***************************************************

Your new generated password is: p3$hJ#8rXa!2
THANK YOU
```

---
