import telebot
from telebot import types
import json

bot = telebot.TeleBot('5808447314:AAEK6Vqqx5TZM-MUgJvldlk-sHGRq4HLqF0')

with open('json.json') as json_file:
    data = json.load(json_file)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name}</b>\nPlease click /help for information'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, "Hi", parse_mode='html')
#     elif message.text == 'ID':
#         bot.send_message(message.chat.id, f'Your ID :{message.from_user.id}', parse_mode='html')
#     elif message.text =='photo':
#         photo = open('photo.jpg','rb')
#         bot.send_photo(message.chat.id, photo)
#     elif message.text[0] =='/':
#         pass
#     else:
#         bot.send_message(message.chat.id,"I don't understand")


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Wow cool')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Check website', url='https://qna.habr.com/q/835815'))
    bot.send_message(message.chat.id, 'Check', reply_markup=markup)


@bot.message_handler(commands=['like'])
def like(message):
    markup = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(f" All {data['likescount']}❤", callback_data='likes'))
    bot.send_message(message.chat.id, "Like me", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def count(call):
    if call.data == 'likes':
        data['likescount'] += 1
        with open('json.json', 'w') as outfile:
            json.dump(data, outfile)
    markup = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(f" All {data['likescount']}❤", callback_data='likes'))

    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    likes = types.KeyboardButton('/like')

    markup.add(website, start,likes)
    bot.send_message(message.chat.id, 'Check', reply_markup=markup)


bot.polling(none_stop=True)
