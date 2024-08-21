# Рассылка писем
def rules(recipient='', sender=''):
    # Функция определяет возможность отправки письма в соответствии с правилами
    # поверяется наличие символа -@
    # проверяется прпавильность написания доменного имени
    send = False
    lst = ('.com', '.ru', '.net')
    if recipient.find('@') != -1 and \
            sender.find('@') != -1 and \
            recipient.endswith(lst) == True and \
            sender.endswith(lst) == True:
        send = True
    return send


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    send = rules(recipient, sender)
    if send == False:
        print('Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient + '.')
    elif sender.strip() == recipient.strip():
        print('Нельзя отправить письмо самому себе!')
    elif sender.strip() == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ' + sender + ' на адрес ' + recipient + '.')
    elif sender.strip() != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ' + sender + ' на адрес ' + recipient + '.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
