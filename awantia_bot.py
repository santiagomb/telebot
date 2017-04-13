# coding=utf-8
import telebot # Importamos las librerías

TOKEN = '365407950:AAEPJlJGVBH-uvHEJF8ZZm6qn9tGszJGo-8' # Ponemos nuestro Token generado con el @BotFather

bot = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API

#tb.send_message('-200039302', 'cagone') # Ejemplo tb.send_message('109556849', 'Hola mundo!')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "ke onda ameo?")

@bot.message_handler(commands=['nee'])
def send_welcome(message):
    bot.reply_to(message, "que dice")

@bot.message_handler(regexp="(l|L)mao")
def handle_message(message):
	bot.send_message('-200039302', 'rofl')

@bot.message_handler(commands=['z6'])
def send_welcome(message):
	bot.send_message('-200039302', "Taking fire, need assistance!")

@bot.message_handler(commands=['c9'])
def send_welcome(message):
	bot.send_message('-200039302', 'La pija!')

@bot.message_handler(regexp="(F|f)acu_")
def send_welcome(message):
	bot.send_message('-200039302', 'navarrooooooooo')

bot.polling()