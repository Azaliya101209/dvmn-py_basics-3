from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage
load_dotenv()


file_name = '''https://dvmn.org/profession-ref-program/azaliyaavzalova09/ash4z/'''
friend_name = '''Луиза'''
sender_name = '''Азалия'''
msg_text = EmailMessage()
msg_text['Subject'] = 'Приглашение!'
msg_text['From'] = 'azaliyaavzalova09@gmail.com'
msg_text['To'] = 'azaliyaavzalova09@gmail.com'
msg_text.set_content("""\
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".replace("%website%",file_name).replace("%my_name%", sender_name).replace("%friend_name%", friend_name))

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(os.environ['LOGIN'], os.environ['PASSWORD'])
    smtp.send_message(msg_text)