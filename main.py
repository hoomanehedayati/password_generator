import passgen
def main():
    password = passgen.insert_pass()
    strength = passgen.password_strenght(password)
    while not passgen.check_password(strength):
        password = passgen.password_generator()
        strength = passgen.password_strenght(password)
    cesar = passgen.caeser_sipher(password)
    print("Your final password is:", cesar)
main()
