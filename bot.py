import config
import telebot
import os
import time


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] != 'ogg':
            continue
        with open('music/'+file, 'rb') as file_handler:
            msg = bot.send_voice(message.chat.id, file_handler, None)
        # А теперь отправим вслед за файлом его file_id
        bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)


if __name__ == '__main__':
    bot.polling(none_stop=True)
