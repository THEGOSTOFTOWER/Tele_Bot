import telebot
from telebot import types
# from classes import Sqliter


bot = telebot.TeleBot('1595628515:AAG3M5kzFWlHmX9BQFCsWquiSqhu6ODkUkM')
id = ''
user_id = ''
mes_id = ''
k = 0
name = ['', '']
st = []
# db = Sqliter('users.db')


@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    global k
    global id
    k = 0
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Переход в главное меню', callback_data='back'))
    bot.send_message(message.chat.id, 'Введите адрес стоянки машины (название улицы с большой буквы (без пр., ул. и т.д.))\n', reply_markup=markup)
    user_id = message.from_user.id
    id = message.chat.id


@bot.message_handler(content_types=['text', 'integer'])
def street(message):
    global name
    global k
    global st
    global user_id
    global id
    if k == 0:
        name[0] = message.text
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='На улице', callback_data='street')
        btn2 = types.InlineKeyboardButton(text='Около дома', callback_data='house1')
        btn3 = types.InlineKeyboardButton(text='Переход в главное меню', callback_data='back')
        markup.row(btn1, btn2)
        markup.row(btn3)
        bot.send_message(id, f'Улица: {name[0]}\n\nВы оставили машину на улице или около дома?\n', reply_markup=markup)
    elif k == 1:
        name[0] = message.text
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='На улице', callback_data='street')
        btn2 = types.InlineKeyboardButton(text='Около дома', callback_data='house1')
        btn3 = types.InlineKeyboardButton(text='Отмена', callback_data='back')
        markup.row(btn1, btn2)
        markup.row(btn3)
        bot.send_message(id, f'Улица: {name[0]}\n\nВы оставили машину на улице или около дома?\n', reply_markup=markup)
    elif k == 2:
        name[1] = message.text
        st.append(name[0] + ' ' + name[1])
        # db.add(user_id, ' '.join(name))
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Добавить стоянку', callback_data='add_stop')
        btn2 = types.InlineKeyboardButton(text='Мои стоянки', callback_data='list_stops')
        if len(st) != 0: # len(db.list(user_id)) != 0
            btn3 = types.InlineKeyboardButton(text='Удалить стоянку', callback_data='del_stops')
            markup.row(btn1, btn3)
        else:
            markup.row(btn1)
        markup.row(btn2)
        bot.send_message(id, 'Главное меню:\n', reply_markup=markup)
    elif k == 3:
        st.remove(st[int(message.text) - 1])  # db.del(user_id, st[int(message.text) - 1])
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Добавить стоянку', callback_data='add_stop')
        btn2 = types.InlineKeyboardButton(text='Мои стоянки', callback_data='list_stops')
        if len(st) != 0:  # len(db.list(user_id)) != 0
            btn3 = types.InlineKeyboardButton(text='Удалить стоянку', callback_data='del_stops')
            markup.row(btn1, btn3)
        else:
            markup.row(btn1)
        markup.row(btn2)
        bot.send_message(id, 'Главное меню:\n', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global user_id
    global name
    global k
    global st
    if call.message:
        if call.data == 'street':
            st.append(name[0])
            # db.add(user_id, name[0])
            markup = telebot.types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text='Добавить стоянку', callback_data='add_stop')
            btn2 = types.InlineKeyboardButton(text='Мои стоянки', callback_data='list_stops')
            if len(st) != 0: # len(db.list(user_id)) != 0
                btn3 = types.InlineKeyboardButton(text='Удалить стоянку', callback_data='del_stops')
                markup.row(btn1, btn3)
            else:
                markup.row(btn1)
            markup.row(btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Главное меню:\n', reply_markup=markup)
        elif call.data == 'house':
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='Отмена', callback_data='back'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Улица: {name[0]}\n\nВведите номер дома\n-Вводить через "-", если, например: 22-18\n'
                                  '-Буква пишется без пробела, например: 37а\n', reply_markup=markup)
            k = 2
        elif call.data == 'house1':
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='Переход в главное меню', callback_data='back'))
            bot.send_message(id, f'Улица: {name[0]}\n\nВведите номер дома\n-Вводить через "-", если, например: 22-18\n'
                             '-Буква пишется без пробела, например: 37а\n', reply_markup=markup)
            k = 2
        elif call.data == 'add_stop':
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='Отмена', callback_data='back'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Введите адрес стоянки машины (название улицы с большой буквы (без пр., ул. и т.д.))\n', reply_markup=markup)
            k = 1
        elif call.data == 'list_stops':
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='Вернуться', callback_data='back'))
            s = ''
            for i in range(1, len(st) + 1):  # st=db.list(user_id)
                s += str(i) + ') ' + st[i - 1] + ' \n'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Ваши стоянки:\n{s}', reply_markup=markup)
        elif call.data == 'del_stops':
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='Отмена', callback_data='back'))
            s = ''
            for i in range(1, len(st) + 1):  # st=db.list(user_id)
                s += str(i) + ') ' + st[i - 1] + ' \n'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Выберете номер удаляемой стоянки:\n{s}', reply_markup=markup)
            k = 3
        elif call.data == 'back':
            markup = telebot.types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text='Добавить стоянку', callback_data='add_stop')
            btn2 = types.InlineKeyboardButton(text='Мои стоянки', callback_data='list_stops')
            if len(st) != 0: # len(db.list(user_id)) != 0
                btn3 = types.InlineKeyboardButton(text='Удалить стоянку', callback_data='del_stops')
                markup.row(btn1, btn3)
            else:
                markup.row(btn1)
            markup.row(btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Главное меню:\n', reply_markup=markup)


bot.polling(none_stop=True)
