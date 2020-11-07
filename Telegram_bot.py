import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == "Hello":
         bot.send_message(message.chat.id, "Hello how can i help you".format(message.chat.id, bot.get_me()), parse_mode='html')
    elif message.text == "I want to watch movie":
        bot.send_message(message.chat.id, "What kind of movie do you want to watch".format(message.chat.id, bot.get_me()),
                         parse_mode='html')
    elif message.text == "What options do you have?":
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=0MQOVrhBERU".format(message.chat.id, bot.get_me()), parse_mode='html')
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=ldERcycPdkk".format(message.chat.id, bot.get_me()), parse_mode='html')

bot.polling(none_stop=True)
