# Домашняя работа по уроку "Способы вызова функции"

def check_correct_address(address_list):
    end_lines = ['com', 'ru', 'net']

    for address in address_list:
        if '@' not in address:
            return True
        if address.split('.')[-1] not in end_lines:
            return True

    return False


def check_sending_yourself(address_list):
    if address_list[0] == address_list[-1]:
        return True


def check_default_sender(sender):
    return sender != 'university.help@gmail.com'


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    address_list = [recipient, sender]

    if check_correct_address(address_list):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif check_sending_yourself(address_list):
        print('Нельзя отправить письмо самому себе!')
    elif check_default_sender(sender):
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
