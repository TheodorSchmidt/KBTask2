user1 = {'name': 'admin', 'password': 'e8#n^cnm29a_$pf1', 'file1.txt': 'write', 'file2.txt': 'write', 'file3.txt': 'write'}
user2 = {'name': 'Rich@rdBrukkk', 'password': '4soper3vq', 'file1.txt': 'write', 'file2.txt': 'read', 'file3.txt': 'read'}
user3 = {'name': 'mr.robot', 'password': 'fs0ciety.dat', 'file1.txt': 'write', 'file2.txt': 'denied', 'file3.txt': 'read'}
user4 = {'name': 'XeniaDbday', 'password': 'rk9s2erf', 'file1.txt': 'denied', 'file2.txt': 'write', 'file3.txt': 'denied'}
user5 = {'name': 'deadAngel', 'password': '1q2w3e4r5t6y', 'file1.txt': 'read', 'file2.txt': 'read', 'file3.txt': 'read'}
data = []
data.append(user1)
data.append(user2)
data.append(user3)
data.append(user4)
data.append(user5)

def FileWork(user, file):
    if user[file] == 'denied':
        print('Вам запрещен доступ к этому файлу')
    elif user[file] == 'read':
        print('Вам разрешено только чтение этого файла. Хотите его открыть? (нажмите 1 на клавиатуре)')
        ans = input()
        if ans == '1':
            f = open(file, 'r')
            for line in f:
                print(line)
            f.close()
            print('Нажмите любую клавишу для продолжения...')
            ans = input()
    elif user[file] == 'write':
        print('Вам разрешены запись и чтение этого файла')
        ans2 = 1
        while ans2 != '0':
            print('Чтобы открыть файл для чтения, нажмите 1. Чтобы открыть файл для записи, нажмите 2. Чтобы закончить работу с файлом, нажмите любую другую клавишу')
            ans2 = input()
            if ans2 == '1':
                f = open(file, 'r')
                for line in f:
                    print(line)
                f.close()
            elif ans2 == '2':
                f = open(file, 'r')
                text = ''
                for line in f:
                    text += line
                f.close()
                f = open(file, 'w')
                inp = input()
                f.write(text + inp)
                f.close()
            else:
                ans = '0'
i = 1;
while (i != '0'):
    print('Добро пожаловать в систему! Чтобы авторизироваться, нажмите 1. Чтобы закрыть, нажмите любую другую клавишу');
    i = input()
    if i == '1':
        print('Введите логин: ')
        log = input()
        print('Введите пароль: ')
        passw = input()
        access = False
        cur_user = {}
        for user in data:
            if user['name'] == log:
                if user['password'] == passw:
                    access = True
                    cur_user = user
        if access == True:
            print(cur_user['name'] + ', вы успешно вошли в систему!')
            i2 = 1;
            while (i2 != '0'):
                print('Чтобы перейти к file[x].txt, нажмите x. Чтобы выйти из аккаунта, нажмите любую другую клавишу')
                i2 = input();
                if (i2 == '1'):
                    FileWork(cur_user, 'file1.txt')
                elif (i2 == '2'):
                    FileWork(cur_user, 'file2.txt')
                elif (i2 == '3'):
                    FileWork(cur_user, 'file3.txt')
                else:
                    i2 = '0'
        else:
            print('Вы ввели неверный логин или пароль')
    else:
        i = '0'