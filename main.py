import telebot
import time

bot = telebot.TeleBot('TOKEN')

def findat(msg):
    #finds the text with "@" from a list of messages
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Welcome ' + message.chat.first_name)

@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.reply_to(message,'To use this bot send a message with a twitter handle')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def twitter(message):
    texts = message.text.split()
    at_text = findat(texts)
    twitter_link = ('twitter.com/{}'.format(at_text[1:]))
    bot.send_message(message.chat.id, twitter_link)
    
@bot.message_handler(func=lambda msg: msg.text is not None and '@' not in msg.text)
def no_command(message):
    bot.reply_to(message, "I dont understand you "+message.chat.first_name)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        time.sleep(15)