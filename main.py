import telebot

import os
import subprocess
import sys
bot = telebot.TeleBot('') #insert api token of your bot in ''


@bot.message_handler(content_types=['photo'])
def image_handler(message):
    chatid = message.chat.id
    path_to_bot = 'C:/Users/Admin/PycharmProjects/PicReturner' #Path to your main.py
    file = bot.get_file(message.photo[-1].file_id)
    #print ("file_id: " + str(message.photo[-1].file_id))
    downloaded_file = bot.download_file(file.file_path)
    #bot.reply_to(message, file.file_path)
    src = path_to_bot + '/' + file.file_path
    new_file = open(src, 'wb+')
    new_file.write(downloaded_file)

    photo_to_send = open(src, "rb")
    bot.send_photo(message.chat.id, photo_to_send, caption='ныа')
    photo_to_send.close()

    new_file.close()

bot.polling()
