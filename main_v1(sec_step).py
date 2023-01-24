import telebot
from telebot import types

bot = telebot.TeleBot('5909930778:AAF4IKk3PqYiTq9hTqQZnr7-ZUAXBttkkAk')


@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Маршрут №1", url='https://yandex.ru/maps/-/CCUzZFVK3D')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Для того чтобы продолжить, выберите маршрут :) \nP.S. Каждый маршрут включает в себя разные места."
                                      "\nК примеру, если вас интересуют музеи в стиле модерн, выберите 'Маршрут "
                                      "№1'.".format(message.from_user), reply_markup=markup)



@bot.message_handler(content_types=['text'])
def start(message):
  if message.text.lower() == '/info':
    kbPhoto = telebot.types.ReplyKeyboardMarkup()
    kbPhoto.row('Получить информацию по первому объекту') #эта и след. строка это название кнопок
    kbPhoto.row('Получить информацию по второму объекту')
    kbPhoto.row('Выйти')
    bot.send_message(message.from_user.id, 'Нажмите на кнопку ниже, чтоб получить информацию.', reply_markup = kbPhoto)
  if message.text.lower() == 'получить информацию по первому объекту': #после нажатия на кнопку, вылезет фотка и текст
    photo = open('2.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo, caption = 'Музей модерна')
    bot.send_message(message.chat.id, "Музей Модерна на территории усадьбы Курлиных – это целостная архитектурно-историческая среда, культурная модель эпохи модерна конца XIX – начала XX веков, времени наивысшего расцвета купеческой Самары."
                                      "\nУсадьбу Курлиных по праву называют «жемчужиной» самарского модерна. Музей Модерна открылся в конце 2012 года, он занимается изучением стиля модерн в регионе, сбором информации и предметов той эпохи")
  if message.text.lower() == 'получить информацию по второму объекту':
    photo = open('1.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo, caption = 'Особняк Э.Г. Эрна')
    bot.send_message(message.chat.id, 'Доктор Эрн, надворный советник, заказал проект дома Щербачёву в 1900 году. Дом был закончен в 1902 году, Эрн переехал в него с семьёй. Часть помещений сдавалась другим докторам под кабинеты и квартиры[1].Так с 1913 года здесь принимал врач Абрам Гринберг – сын доктора М. А. Гринберга, а другой сын Иосиф Гринберг – присяжный поверенный самарского окружного суда - снимал апартаменты[2].В 1920-е годы в бывшем доме Эрна находилось отделение самарской ВЧК (позже ОГПУ)[1]. В 1941—1943 году в здании размещалось эвакуированное из Москвы посольство Польши. В частности, в этом здании 4 декабря 1941 года наркомом иностранных дел СССР В. М. Молотовым и председателем правительства Польши в изгнании В. Сикорским была подписана Декларация «О достижении прочного и справедливого мира»[3][4]. Впоследствии особняк вошёл в состав комплекса Самарской областной клинической больницы № 2, в нем расположена поликлиника[4].')

  if message.text.lower() == 'выйти':
    bot.send_message(message.from_user.id, 'Клавиатура убрана.', reply_markup = types.ReplyKeyboardRemove())


@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, 'Привет, для начала работы напишите /start')


bot.polling(none_stop=True)