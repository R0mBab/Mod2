import re


def send_email(message,recipient, sender = "university.help@gmail.com"):
    if not sender.find("@") and recipient.find("@") or not re.findall('.com|.ru|.net', (recipient and sender)) :
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if sender == recipient and recipient == "university.help@gmail.com" :
        print(f"Нельзя отправить письмо самому себе!")
    if sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')