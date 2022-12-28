from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = '5675428773:AAHvZmpr1aR1OmksquUQSfteh1tGjMaQWLw'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!\nBu bot lotin matni kiritilsa kirilchaga, Kiril matni kiritilsa lotinchaga o'girib beradi!"
    javob += "\nEhtiyot bo'ling, agar lotin, kiril matn aralash kiritilsa u har doim lotinchaga o'giradi!"
    javob += '\nMatn kiriting: '
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg  = message.text
    if msg.isascii():
        yangi_matn = to_cyrillic(msg)
    else:
        yangi_matn = to_latin(msg)
    bot.reply_to(message, yangi_matn)

bot.polling()

