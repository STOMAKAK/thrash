import telebot
import random
import os 

API_TOKEN = '8028458172:AAGy77N2fKNvEFEKXByxaMTGqkgxKHrDYw0'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['mem', 'мемы'])
def echo_message(message):
    images = random.choice(os.listdir("images"))
    with open('images/' + images, 'rb') as f:
        bot.send_photo(message.chat.id, f)
        

@bot.message_handler(commands=['meme'])
def echo_message(message):
    images = random.choice(os.listdir("meme"))
    with open('meme/' + images, 'rb') as f:
        bot.send_photo(message.chat.id, f)
        
    
@bot.message_handler(commands=['plastic'])
def send_welcome(message):
    bot.reply_to(message, """
1. Нарисуйте отверстие радиусом 1 см на расстоянии 10 см от дна.
2. Поверните бутылку на 90 градусов и нарисуйте еще одно отверстие радиусом 2 см, напротив первого.
3. Этот же процесс нужно повторить на расстоянии 5 см от дна.
4. После чего аккуратно вырежьте ножом все нарисованные отверстия.
5. Теперь можно вставлять ложки.
6. Чтобы подвесить бутылку необходимо прикрутить винтик или шуруп к крышке бутылки и подвесить ее на веревку.
7. Наконец, можно заполнять Ваш резервуар птичьим кормом.""")
    bot.send_photo(message.chat.id, "https://www.infoniac.ru/upload/medialibrary/8ba/8ba09f8c8aaa59d3862506441e9c9bd1.jpg")
    
    
@bot.message_handler(commands=['crocodile'])
def send_welcome(message):
    bot.reply_to(message, """
1. Ножом и ножницами обрежьте бутылки пополам, затем обрежьте одну часть так, чтобы оставалась высота 7 см.
2. Обрежьте края бутылок так, чтобы крокодил был согнут.
3. Приклейте ножки-крышки к крокодилу равномерно.
4. Сделайте плотные шарики из бумаги и прикрепите их как глазки крокодила.
5. Обклейте весь корпус тонкой зеленой бумагой.
6. Вырежьте из парафированной бумаги и приклейте лапки, глаза и зубы. Покрасьте зубы в белый цвет, а ноздри и глаза в черный.""")
    bot.send_photo(message.chat.id, "https://www.infoniac.ru/upload/medialibrary/622/622ae72ee396082999638b0daf615357.jpg")

@bot.message_handler(commands=['problem'])
def send_welcome(message):
    bot.reply_to(message, """Заводы, выпускающие пластиковые изделия, выделяют в атмосферу до 400 миллионов тонн углекислого газа в год и примерно 800 видов животных сегодня находятся под угрозой вымирания из-за поедания и отравления пластиком. Одноразовые пакеты забивают канализационные системы городов и создают угрозы наводнений, пластмассовый мусор засоряет берега и прибрежные зоны, предназначенные для для отдыха, нанося урон туристический отрасли.""")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """
Это @makakmem_bot я расскажу о проблемах с загрязнением и о красивых поделках из пластика
1) /crocodile - пришлю инструкцию по изготовлению пластикого крокодильчика
2) /problem - я расскажу о проблеме загрязнения на Земле
3) /plastic - объясню как сделать кормушку для птичек из пластиковой бутылки
""")
    
    
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()