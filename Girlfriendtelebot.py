# Подключаем модуль случайных чисел
import random

# Подключаем модуль для Телеграма
import telebot

# Указываем токен
bot = telebot.TeleBot('1487122552:AAGF8UugtdUTZbylEt8Mjo_n76JHdSJn1gY')

# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Заготовки для трёх предложений
first = ["Я НЕ ВИДЕЛАСЬ С РОДСТВЕННИКАМИ И СТАРЫМИ ДРУЗЬЯМИ ЦЕЛУЮ ВЕЧНОСТЬ! ВЕЧНОСТЬ ИЗ-ЗА ТЕБЯ! КАК ТЫ МОЖЕШЬ УПРЕКАТЬ МЕНЯ В ЭТОМ?!"]
second = ["Стало лучше, когда ты написал ^_^"]


# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Так то лучше, пушистик! Я чёт так накидалась на НГ")
        keyboard = types.InlineKeyboardMarkup()
    # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Охренела?!', callback_data='Охренела')
    # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Как себя чувствуешь, зай?', callback_data='Как себя чувствуешь, зай')
        keyboard.add(key_telec)
        bot.send_message(message.from_user.id, text='Совершенно ничего не помню =( ', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Напиши нормально! Ты не можешь просто написать Привет?")

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):
    # Если нажали на одну из кнопок — выводим гороскоп
    if call.data == 'Охренела':
        # Формируем гороскоп
        msg = first
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'Как себя чувствуешь, зай':
        # Формируем гороскоп
        msg = second
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)




# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
