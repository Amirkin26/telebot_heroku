from telebot import TeleBot
import config
from telebot.types import ReplyKeyboardMarkup

bot = TeleBot(config.token)
keyboard = ReplyKeyboardMarkup(True)
keyboard.row('/start','/info')
keyboard.row('Привет','Пока')
stickerStart = 'CAACAgIAAxkBAALupmBDzs8WucoXTs7lk5Mb6tcYBGhZAAJ0AAM7YCQUs8te1W3kR_QeBA'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(message.chat.id,stickerStart)
    print(message.chat.id, message.text)
    bot.send_message(message.chat.id,"Привет {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),parse_mode='html')
@bot.message_handler(commands=['info'])
def start(message):
    print(message.chat.id, message.text)
    bot.send_message(message.chat.id,'Ich bin hier alleine ?',reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def lalala(message):
    print(message.chat.id,message.text)
    bot.send_message(message.chat.id, message.text,reply_markup=keyboard)

bot.polling(none_stop=True)




