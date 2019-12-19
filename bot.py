import telebot
import time

bot_token = '678462892:AAHzUIxRLhlqlTcov66bOpStudJqlM72SO8'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)    

bot.polling()