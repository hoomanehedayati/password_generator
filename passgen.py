
import random
alphabet = ["A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z" ,"1", "2", "3", "4", "5", "6", "7", "8", "9","!", "@", "#", "$", "%", "^", "&", "*","-", "_", "+", "=", "/", "|", "?","<", ">", "[", "]", "{", "}", "~", "`",":", ";", "'", '"', ",", "."]
def password_generator():
    password = ""
    numcharacter = int(input("How many characters do you want (choose more than 12)? "))
    while numcharacter < 12:
        print("Choose at least 12 characters!")
        numcharacter = int(input("How many characters do you want? "))
    password += random.choice(alphabet[:26])
    password += random.choice(alphabet[26:52])
    password += random.choice(alphabet[52:61])
    password += random.choice(alphabet[61:])
    for i in range(numcharacter - 4):
        index = random.randint(0, len(alphabet)-1)
        password += alphabet[index]
    password = ''.join(random.sample(password, len(password)))
    return password
def password_strenght(checkpass):
    score = 0
    if len(checkpass) >= 12:
        score += 1
    for char in checkpass:
        if char.isupper():
            score += 1
            break
    for char in checkpass:
        if char.islower():
            score += 1
            break
    for char in checkpass:
        if char.isdigit():
            score += 1
            break
    for char in checkpass:
        if not char.isalnum():
            score += 1
            break
    if score <= 2:
        strength = "weak"
    elif score <= 4:
        strength = "medium"
    else:
        strength = "strong"
    return strength
def check_password(strength):
    isok = True
    if strength != "strong":
        isok = False
        print("Your password is not strong enough, we will make one for you")
    return isok
def caeser_sipher(password):
    yesorno = input("Do you want to implement caeser sipher for your password? ")
    if yesorno == "yes":
        encrypted_password = ""
        shift = int(input("Enter the shift number: "))
        for char in password:
            if char in alphabet[:52]:
                index = alphabet.index(char)
                new_index = (index + shift) % 26
                if char.islower():
                    new_index += 26
                encrypted_password += alphabet[new_index]
            else:
                encrypted_password += char
        return encrypted_password
    else:
        return password
def insert_pass():
    passs = input("Insert your password: ")
    return passs
