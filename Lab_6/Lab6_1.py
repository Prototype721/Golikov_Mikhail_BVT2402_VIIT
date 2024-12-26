class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        self.__password_hash = hash(password)

    def set_password(self, new_password):
        self.__password = new_password
        self.__password_hash = hash(new_password)
        return True
    
    def check_password(self, password):
        #if hash(password) == self.__password_hash:
        if password == self.__password:
            return True
        return False

Root = UserAccount(username='Admin', email=None, password='sudo')

check = Root.check_password("sudo")
print(f'sudo for check - {check}')

print('-'*40)

check = Root.check_password('qwerty')
print(f'qwerty for check - {check}')

print('-'*40)

new_psw = input('Set new password: ')
Root.set_password(new_psw)
print(f'New password set to {new_psw}')

print('-'*40)

new_psw_check = input('Check password: ')
print(f'{new_psw_check} for check - {Root.check_password(new_psw_check)}')

new_psw_check = input('Check password: ')
print(f'{new_psw_check} for check - {Root.check_password(new_psw_check)}')