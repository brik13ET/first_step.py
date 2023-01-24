import telebot
from telebot import types

bot = telebot.TeleBot('5909930778:AAF4IKk3PqYiTq9hTqQZnr7-ZUAXBttkkAk')


@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Маршрут №1", url='https://yandex.ru/maps/-/CCUzFTcQ0D')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на выбранную кнопку и окунись в атмосферу модерна)".format(message.from_user), reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, 'Привет, я тебя не понимаю:) для начала работы напишите /start')



bot.polling(none_stop=True)