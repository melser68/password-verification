import re
import string

pass_patern_lower = re.compile(fr'[{string.ascii_lowercase}+]')
pass_pattern_upper = re.compile(fr'[{string.ascii_uppercase}+]')
pass_pattern_punctuation = re.compile(fr'[{string.punctuation}+]')
pass_pattern_digits = re.compile(r'[0-9]+')


def check_password(password:str) ->str:
    if len(password) < 8:
        return 'Password is short (minimal 8 characters)'
    else:
        result = []
        if not pass_patern_lower.findall(password):
            result.append('No symbols lower')
        if not pass_pattern_upper.findall(password):
            result.append('No symbols upper')
        if not pass_pattern_punctuation.findall(password):
            result.append('No special symbols')
        if not pass_pattern_digits.findall(password):
            result.append('No digits')
        if len(result) == 0:
            return f'Password: "{password}" - is correct !'
        else:
            return f'!!!Password "{password}" is not correct!!!\n={" ; ".join(result)}='
        

if __name__ == '__main__':
    print('===Rules for password - min 9 characters, chars upper, chars lower, special symbols===')
    while True:
        password = input('Input your password for checking:\n>>>>  ')
        print(check_password(password))
        choice = input('Repeat ? (yes/no)\n>>>>  ')
        if choice.lower() == 'no':
            break

