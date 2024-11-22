def send_email(message, recipient, sender = "university.help@gmail.com" ):
    tulpan = ['.com' , '.ru' , '.net']
    add = 0
    for i in tulpan:
        if ('@' and i) not in (sender or recipient):
            add = add + 1
            if add > 2:
                print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
                return
        else:
            break
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        return
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient,".")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')