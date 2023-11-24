import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import pyowm
from gtts import gTTS
from pydub import AudioSegment
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import sqlite3

# Создаем объект Updater с указанием токена вашего бота
updater = Updater(token='6751801078:AAGCIMo3gpCy7uUVKlJNQRyKUOU1C__XwNk')

# Получаем объект Dispatcher для регистрации обработчиков
dispatcher = updater.dispatcher

# Функция-обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a bot!")

# Функция-обработчик команды /help
def help(update, context):
    text = "Available commands:\n/start – start the bot\n/help – show available commands"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# Функция-обработчик текстовых сообщений
def message_handler(update, context):
    text = update.message.text.lower()
    if text == 'hi':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")

# Регистрируем обработчики команд и сообщений
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

# Запускаем процесс обновления
updater.start_polling()

# Оставшаяся часть вашего кода (обработчики команд /quote, /cat, и так далее) остается без изменений.

# Не забудьте заменить 'YOUR_BOT_TOKEN_HERE' на актуальный токен вашего бота.
