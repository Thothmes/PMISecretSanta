import telebot
from datetime import datetime
import random

TOKEN = "6329741208:AAHyfTJrSQ4bYGKi8o9RwpMQHJxSm_IPRb8"
bot = telebot.TeleBot(TOKEN)

happy_students = [];pary_studentov = []

@bot.message_handler(content_types=['text'])

def comands(message):

    if message.text == "/start":

        bot.send_message(message.from_user.id, "Привет, этот бот поможет тебе вместе с твоими друзьями сыграть в Тайного Санту! Вот комманды:"
                                    f"\n/add_student [Имя студента]- Добавить студента в Игру"
                                    f"\n/del_student [Имя студента]- Убрать студента из игры"
                                    f"\n/SecretSantaStart - Начать распределение! Да будет праздник"
                                    )
    
    if "/add_student" in message.text:
        def add_student():
            student = str(message.text).split()
            if student[1] not in happy_students:
                happy_students.append(student[1])
                bot.send_message(message.from_user.id, "Отлично! Теперь этот студент получит подарок!")
            else:
                bot.send_message(message.from_user.id, "Прости, но такой студент уже участвует в Тайном Санте."
                                 "\nЕсли студент точно не записан, то попробуй ввести его имя с фамилией или обозначением!")
            print(student[1])
        add_student()

    if "/del_student" in message.text:

        def del_student():
            student = str(message.text).split()
            if student[1] in happy_students:
                for i in range(0,len(happy_students)):
                    if happy_students[i] == student[1]:
                        happy_students.remove(happy_students[i])
                bot.send_message(message.from_user.id, "Эх, а ведь такой подарок мог быть! Впрочем, теперь он достанется кому-нибудь другому!")
            else:
                bot.send_message(message.from_user.id, "Прости, но такой студент не участвует в Тайном Санте")
            print(student[1])

        bot.send_message(message.from_user.id, "Таак, напиши имя студента, который отказался играть!")
        del_student()

    if message.text == "/SecretSantaStart":

        bot.send_message(message.from_user.id, "Наконец-то! Мы начинаем! Хо-хо-хо!")
        if len(happy_students) % 2 == 0:
            student_dop_array = happy_students
            while student_dop_array != []:
                student_1 = random.choice(student_dop_array)
                student_dop_array.remove(student_1)
                student_2 = random.choice(student_dop_array)
                student_dop_array.remove(student_2)
                student_str = str(student_1 + " " + "и" + " " + student_2)
                pary_studentov.append(student_str)
                student_str = str()
            for i in range(0,len(pary_studentov)):
                bot.send_message(message.from_user.id, "А вот и наши студенты, что должны будут подарить друг-другу подарочки!:")
                bot.send_message(message.from_user.id, pary_studentov[i])
            bot.send_message(message.from_user.id, "Хо-хо-хо! Удачных вам праздников! Дарите друг-другу радость, позитив и тёплые воспоминания!")


        else:
            bot.send_message(message.from_user.id, "Прости дружище, но кто-то из студентов похоже рискует остаться без подарка, а это недопустимо!"
                                "\nДобавь ещё кого-нибудь, что бы все смогли получить радость и веселье!")
            
bot.polling()
