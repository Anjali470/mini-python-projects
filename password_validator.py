def password_validator(password):
    special_chars = '!@#$%^&*'
    if len(password) < 8:
        return False, 'Minimum 8 characters required!!'
    if not any(char.isupper() for char in password):
        return False, "Atleast one uppercase letter is required"
    if not any(char.islower() for char in password):
        return False, 'Atleast one lowercase letter is required'
    if not any(char.isdigit() for char in password):
        return False, 'Atleast one number is required'
    if not any (char in special_chars for char in password):
        return False, 'Atleast one special character is required'
    else:
        return True, 'Password is strong!!'

def main():
    password = input("Enter your password: ")
    is_valid, message = password_validator(password)
    print(f'{is_valid}, {message}')

if __name__ == '__main__':
    main()